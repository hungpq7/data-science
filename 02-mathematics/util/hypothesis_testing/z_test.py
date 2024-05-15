import numpy as np
import scipy.stats as stats
from .base_test import BaseTest

class MeanZTest(BaseTest):
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
        self.n1 = self.x1.size
        self.mean1 = self.x1.mean()

        if self.type == '1-sample':
            self.n2 = np.inf
            self.mean2 = 0
            self.var2 = 0
        elif self.type == '2-sample':
            self.n2 = self.x2.size
            self.mean2 = self.x2.mean()
        
        se = np.sqrt(self.var1 / self.n1 + self.var2 / self.n2)
        self.test_stat = (self.mean1 - self.mean2 - self.const) / se
    
    def _set_dist(self):
        self.dist = stats.norm()

class ProportionZTest(BaseTest):
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
        if self.type == '1-sample':
            self.p2 = 0
            self.n2 = np.inf
        
        se = self.p1 * (1 - self.p1) / self.n1 
        se += self.p2 * (1 - self.p2) / self.n2
        se = np.sqrt(se)
        self.test_stat = (self.p1 - self.p2 - self.const) / se

    def _set_dist(self):
        self.dist = stats.norm()