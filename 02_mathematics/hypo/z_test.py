import numpy as np
import scipy.stats as stats

from .base import BaseTest

class PropTest(BaseTest):
    def __init__(self, prop, size, const=0, **kwargs):
        super().__init__(**kwargs)
        self.prop = prop
        self.size = size
        self.const = const

        if isinstance(size, (list, tuple, np.ndarray)) and len(size) == 2:
            self.type = '2-sample'
            self.objective = 'p1 - p2'

        elif isinstance(size, (float, int)):
            self.type = '1-sample'
            self.objective = 'p'
    
    @classmethod
    def from_data(cls, x1, x2=None, **kwargs):
        if x2 is None:
            prop = np.mean(x1)
            size = len(x1)
        else:
            prop = np.mean(x1), np.mean(x2)
            size = len(x1), len(x2)
        return cls(prop=prop, size=size, **kwargs)

    def _compute_stats(self):
        if self.type == '1-sample':
            p1, n1 = self.prop, self.size
            p2, n2 = 0, np.inf

        elif self.type == '2-sample':
            p1, n1 = self.prop[0], self.size[0]
            p2, n2 = self.prop[1], self.size[1]

        se = p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2
        se = np.sqrt(se)
        self.test_stat = (p1 - p2 - self.const) / se

    def _set_dist(self):
        self.dist = stats.norm()