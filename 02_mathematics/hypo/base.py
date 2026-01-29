from dataclasses import dataclass
import io
from IPython.display import display, SVG

import numpy as np
import matplotlib.pyplot as plt

@dataclass
class BaseTest:
    const: float = 0
    alternative: str = '!='
    alpha: float = 0.05

    # placeholders
    objective: str = None
    ndim: int = None
    test_stat: float = None
    dist: object = None
    p_value: float = None
    sign_test: str = None
    h0_conclusion: str = None
    
    def _compute_stats(self):
        self.test_stat = None
    
    def _set_dist(self):
        self.dist = None

    def _compute_pvalue(self):
        if self.alternative == '!=':
            self.p_value = self.dist.sf(abs(self.test_stat)) * 2

        elif self.alternative == '>':
            self.p_value = self.dist.sf(self.test_stat)

        elif self.alternative == '<':
            self.p_value = self.dist.cdf(self.test_stat)

    def _make_decision(self):
        if self.p_value <= self.alpha:
            self.sign_test = '<'
            self.h0_conclusion = 'REJECT'

        elif self.p_value > self.alpha:
            self.sign_test = '>'
            self.h0_conclusion = 'ACCEPT'

    def conduct(self, print_result=True):
        self._compute_stats()
        self._set_dist()
        self._compute_pvalue()
        self._make_decision()

        if print_result is True:
            print(
                f'Alternative Hypothesis (H1): {self.objective} {self.alternative} {self.const}\n'
                f'p-value = {self.p_value:.4f} {self.sign_test} {self.alpha} --> {self.h0_conclusion} H0'
            )
    
    def plot(self):
            if self.dist is None or self.p_value is None:
                print("Please run .conduct() before plotting.")
                return

            fig, ax = plt.subplots(figsize=(6, 4))
            
            # 1. Define x-range (covering 99.9% of the distribution)
            x = np.linspace(self.dist.ppf(0.001), self.dist.ppf(0.999), 500)
            y = self.dist.pdf(x)
            ax.plot(x, y, color='grey', ls='-', lw=2, label=f'{self.dist.dist.name.title()} distribution')
            ax.axhline(0, color='grey', linestyle='--', lw=1)

            # 2. Handle Rejection Regions based on the Alternative Hypothesis
            if self.alternative == '!=':
                cv_low = self.dist.ppf(self.alpha / 2)
                cv_high = self.dist.ppf(1 - self.alpha / 2)
                
                x_left = np.linspace(x.min(), cv_low, 100)
                x_right = np.linspace(cv_high, x.max(), 100)
                
                ax.fill_between(x_left, self.dist.pdf(x_left), color='darkorange', alpha=0.3, label='Rejection region')
                ax.fill_between(x_right, self.dist.pdf(x_right), color='darkorange', alpha=0.3)
                ax.axvline(cv_low, color='darkorange', linestyle='--', lw=1)
                ax.axvline(cv_high, color='darkorange', linestyle='--', lw=1)

            elif self.alternative == '>':
                cv = self.dist.ppf(1 - self.alpha)
                x_rej = np.linspace(cv, x.max(), 100)
                ax.fill_between(x_rej, self.dist.pdf(x_rej), color='darkorange', alpha=0.3, label='Rejection region')
                ax.axvline(cv, color='darkorange', linestyle='--', lw=1)

            elif self.alternative == '<':
                cv = self.dist.ppf(self.alpha)
                x_rej = np.linspace(x.min(), cv, 100)
                ax.fill_between(x_rej, self.dist.pdf(x_rej), color='darkorange', alpha=0.3, label='Rejection region')
                ax.axvline(cv, color='darkorange', linestyle='--', lw=1)

            ax.axvline(self.test_stat, color='indianred', lw=2, label=f'Test stat: {self.test_stat:.2f}')
            
            ax.set_xlabel('Value')
            ax.set_ylabel('Probability Density')
            ax.legend()
            ax.grid(False)

            f = io.StringIO()
            plt.savefig(f, format='svg')
            plt.close(fig)
            display(SVG(f.getvalue()))