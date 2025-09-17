import numpy as np
import scipy.stats as stats
from .base import BaseTest

class ZTestMean(BaseTest):
    def __init__(self, x1, var1, x2=None, var2=None, const=0, **kwargs):
        super().__init__(**kwargs)
        self.x1 = np.array(x1)
        self.var1 = var1
        self.x2 = np.array(x2)
        self.var2 = var2
        self.const = const

        if self.x2 is not None and self.var2 is not None:
            self.type = '2-sample'
            self.objective = 'mean1 - mean2'
        else:
            self.type = '1-sample'
            self.objective = 'mean'

    def _compute_stats(self):
        n1 = self.x1.shape[0]
        mean1 = self.x1.mean()
        var1 = self.var1

        if self.type == '1-sample':
            n2 = np.inf
            mean2 = 0
            var2 = 0
        elif self.type == '2-sample':
            n2 = self.x2.shape[0]
            mean2 = self.x2.mean()
            var2 = self.var2
        
        se = np.sqrt(var1 / n1 + var2 / n2)
        self.test_stat = (mean1 - mean2 - self.const) / se
    
    def _set_dist(self):
        self.dist = stats.norm()

class ZTestProportion(BaseTest):
    def __init__(self, p1, n1, p2=None, n2=None, const=0, **kwargs):
        super().__init__(**kwargs)
        self.p1 = p1
        self.n1 = n1
        self.p2 = p2
        self.n2 = n2
        self.const = const

        if self.n2 is not None and self.p2 is not None:
            self.type = '2-sample'
            self.objective = 'p1 - p2'
        else:
            self.type = '1-sample'
            self.objective = 'p'
    
    def _compute_stats(self):
        p1 = self.p1
        n1 = self.n1

        if self.type == '1-sample':
            p2 = 0
            n2 = np.inf
        else:
            p2 = self.p2
            n2 = self.n2
        
        se = p1 * (1 - p1) / n1 
        se += p2 * (1 - p2) / n2
        se = np.sqrt(se)
        self.test_stat = (p1 - p2 - self.const) / se

    def _set_dist(self):
        self.dist = stats.norm()