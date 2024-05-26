import numpy as np
import pandas as pd
import scipy.stats as stats
from .base import BaseTest

class Chi2DependenceTest(BaseTest):
    def __init__(self, x1, x2, **kwargs):
        super().__init__(**kwargs)
        self.x1 = x1
        self.x2 = x2
        self.objective = ''