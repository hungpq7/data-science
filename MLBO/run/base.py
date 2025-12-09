import time

import numpy as np
import torch
from torch import Tensor

from botorch.fit import fit_gpytorch_mll
from botorch.models import SingleTaskGP
from botorch.models.transforms.input import Normalize
from botorch.models.transforms.outcome import Standardize
from botorch.optim import optimize_acqf
from gpytorch.mlls import ExactMarginalLogLikelihood

torch.manual_seed(0)
torch.set_default_dtype(torch.double)

class BaseOptimizer:
    def __init__(
        self,
        blackbox=None,
        n_init=10,
        max_iter=50,
        batch_size=1,
    ):
        self.blackbox = blackbox
        self.dim = blackbox.dim
        self.bounds = blackbox.bounds
        self.n_init = n_init
        self.batch_size = batch_size

    def gen_initial_data(self, size, dim):
        x_train = torch.rand(size, dim, dtype=torch.double)
        y_train = self.blackbox(x_train).unsqueeze(-1)
        return x_train, y_train

    def build_model(self, x_train, y_train):
        model = SingleTaskGP(
            x_train, y_train,
            input_transform=Normalize(d=self.dim),
            outcome_transform=Standardize(m=1),
        )
        mll = ExactMarginalLogLikelihood(model.likelihood, model)
        return model, mll

    def fit_model(self, x_train, y_train, state_dict=None):
        model, mll = self.build_model(x_train, y_train)
        if state_dict is not None:
            # Load previous GP's parameters for warm start
            model.load_state_dict(state_dict)
        
        # Fit the model with LBFGS-B
        fit_gpytorch_mll(mll)

        # Save updated GP's parameters to warm start next iteration
        new_state_dict = model.state_dict()
        return model, mll, new_state_dict
    
    def gen_new_candidate(self, model, best_f, **kwargs):
        x_new = torch.rand(1, self.dim, dtype=torch.double)
        y_new = self.blackbox(x_new).unsqueeze(-1)
        return x_new, y_new
    
    def run_bo(self, print_every=1, **kwargs):
        start = time.time()

        x_train, y_train = self.gen_initial_data(self.n_init, self.dim)
        model, mll, state_dict = self.fit_model(x_train, y_train)

        n_iter = (self.max_iter - self.n_init) // self.batch_size
        for i in range(n_iter):
            best_f = y_train.max().item()
            x_new, y_new = self.gen_new_candidate(model, best_f, **kwargs)

            x_train = torch.cat([x_train, x_new], dim=0)
            y_train = torch.cat([y_train, y_new], dim=0)

            # Rebuild + warm-start + refit on all data
            model, mll, state_dict = self.fit_model(x_train, y_train, state_dict=state_dict)

            if print_every > 0:
                if (i+1) % print_every == 0:
                    y_best = y_train.max().item()
                    print(f"Iter {i+1} | Current best: {y_best:.4f}")

        duration = time.time() - start
        return y_best, duration
    
    def benchmark(self, runs=10, **kwargs):
        best_vals = []
        durations = []

        for run in range(runs):
            best_val, duration = self.run_bo(**kwargs)
            best_vals.append(best_val)
            durations.append(duration)

        return np.array(best_vals), np.array(durations)

class EIOptimizer(BaseOptimizer):
    def gen_new_candidate(self, model, best_f, **kwargs):
        from botorch.acquisition.analytic import ExpectedImprovement
        acqf = ExpectedImprovement(model=model, best_f=best_f, maximize=True)

        x_new, _ = optimize_acqf(
            acq_function=acqf,
            bounds=self.bounds,
            q=self.batch_size,
            num_restarts=10,
            raw_samples=128,
        )

        y_new = self.blackbox(x_new).unsqueeze(-1)
        return x_new, y_new

class qEIOptimizer(BaseOptimizer):
    def gen_new_candidate(self, model, best_f, **kwargs):
        from botorch.acquisition.monte_carlo import qExpectedImprovement
        acqf = qExpectedImprovement(model=model, best_f=best_f, maximize=True)

        x_new, _ = optimize_acqf(
            acq_function=acqf,
            bounds=self.bounds,
            q=self.batch_size,
            num_restarts=10,
            raw_samples=128,
        )

        y_new = self.blackbox(x_new).unsqueeze(-1)
        return x_new, y_new

class OptimizerFactory:
    @staticmethod
    def produce(name, **kwargs):
        map_optimizer = {
            "Base": BaseOptimizer,
            "aEI": EIOptimizer,
        }

        optimizer = map_optimizer.get(name)
        if optimizer is not None:
            return optimizer(**kwargs)
        else:
            raise ValueError(f"Unknown optimizer name: {name}")