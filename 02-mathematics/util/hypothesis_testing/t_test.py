import numpy as np
import scipy.stats as stats
from .base import BaseTest

class TTestOneSample(BaseTest):
    def __init__(self, x, const=0, **kwargs):
        super().__init__(**kwargs)
        self.x = np.array(x)
        self.const = const
        self.objective = 'mean'
    
    def _compute_stats(self):
        mean = self.x.mean()
        var = self.x.var(ddof=1)
        n = self.x.shape[0]
        self.test_stat = (mean - self.const) / np.sqrt(var / n)
        self.dof = n - 1
    
    def _set_dist(self):
        self.dist = stats.t(self.dof)

class TTestIndSample(BaseTest):
    def __init__(self, x1, x2, const=0, **kwargs):
        super().__init__(**kwargs)
        self.x1 = x1
        self.x2 = x2
        self.const = const
        self.objective = 'mean1 - mean2'

    def _compute_stats(self):
        scipy_result = stats.ttest_ind(self.x1, self.x2, equal_var=True, alternative=self.alternative)
        self.test_stat = scipy_result.statistic
        self.dof = scipy_result.df
    
    def _set_dist(self):
        self.dist = stats.t(self.dof)