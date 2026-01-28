import numpy as np
import scipy.stats as stats

from .base import BaseTest

class MeanTest(BaseTest):
    def __init__(self, mean, var, size, const=0, equal_var=None, **kwargs):
        super().__init__(**kwargs)
        self.mean = mean
        self.var = var
        self.size = size
        self.const = const
        self.equal_var = equal_var

        if isinstance(size, (list, tuple, np.ndarray)) and len(size) == 2:
            self.type = '2-sample'
            self.objective = 'mean1 - mean2'

        elif isinstance(size, (float, int)):
            self.type = '1-sample'
            self.objective = 'mean'
    
    @classmethod
    def from_data(cls, x1, x2=None, **kwargs):
        if x2 is None:
            mean = np.mean(x1)
            var = np.var(x1, ddof=1)
            size = len(x1)
        else:
            mean = np.mean(x1), np.mean(x2)
            var = np.var(x1, ddof=1), np.var(x2, ddof=1)
            size = len(x1), len(x2)
        return cls(mean, var, size, **kwargs)

    def _compute_stats(self):
        if self.type == '1-sample':
            se = np.sqrt(self.var / self.size)
            self.test_stat = (self.mean - self.const) / se
            self.dof = self.size - 1

        elif self.type == '2-sample':
            mean1, mean2 = self.mean
            var1, var2 = self.var
            size1, size2 = self.size

            if self.equal_var is None:
                self.equal_var = np.isclose(var1, var2)

            if self.equal_var is True:
                pooled_var = ((size1 - 1) * var1 + (size2 - 1) * var2) / (size1 + size2 - 2)
                se = np.sqrt(pooled_var * (1 / size1 + 1 / size2))
                self.test_stat = (mean1 - mean2 - self.const) / se
                self.dof = size1 + size2 - 2

            elif self.equal_var is False:
                se = np.sqrt(var1 / size1 + var2 / size2)
                self.test_stat = (mean1 - mean2 - self.const) / se
                num = (var1 / size1 + var2 / size2) ** 2
                denom = ((var1 / size1) ** 2) / (size1 - 1) + ((var2 / size2) ** 2) / (size2 - 1)
                self.dof = num / denom
    
    def _set_dist(self):
        self.dist = stats.t(self.dof)