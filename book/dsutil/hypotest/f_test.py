import numpy as np
import scipy.stats as stats
from .base import BaseTest

class FTest(BaseTest):
    def __init__(self, x1, x2, const=0, **kwargs):
        super().__init__(**kwargs)
        self.x1 = np.array(x1)
        self.x2 = np.array(x2)
        self.const = const
        self.objective = 'var1 / var2'
    
    def _compute_stats(self):
        var1 = self.x1.var()
        var2 = self.x2.var()
        self.test_stat = var1 / var2 / self.const
        self.dof1 = self.x1.shape[0] - 1
        self.dof2 = self.x2.shape[0] - 1
    
    def _set_dist(self):
        self.dist = stats.f(self.dof1, self.dof2)