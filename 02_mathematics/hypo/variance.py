import numpy as np
import scipy.stats as stats

from .base import BaseTest

class VarianceTest(BaseTest):
    def __init__(self, var, size, const=1, **kwargs):
        super().__init__(**kwargs)
        self.var = var
        self.size = size
        self.const = const

        if isinstance(var, (list, tuple, np.ndarray)) and len(var) == 2:
            self.ndim = 2
            self.objective = 'var1 / var2'

        elif isinstance(var, (float, int)):
            self.ndim = 1
            self.objective = 'var'
    
    @classmethod
    def from_data(cls, x1, x2=None, **kwargs):
        if x2 is None:
            var = np.var(x1, ddof=1)
            size = len(x1)
        else:
            var = np.var(x1, ddof=1), np.var(x2, ddof=1)
            size = len(x1), len(x2)
        return cls(var, size, **kwargs)

    def _compute_stats(self):
        if self.ndim == 1:
            self.test_stat = (self.size - 1) * self.var / self.const
            self.dof = self.size - 1

        elif self.ndim == 2:
            var1, var2 = self.var
            size1, size2 = self.size
            self.test_stat = (var1 / var2) / self.const
            self.dof1 = size1 - 1
            self.dof2 = size2 - 1

    def _set_dist(self):
        if self.ndim == 1:
            self.dist = stats.chi2(self.dof)

        elif self.ndim == 2:
            self.dist = stats.f(self.dof1, self.dof2)
