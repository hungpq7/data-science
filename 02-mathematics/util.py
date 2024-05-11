import warnings
warnings.filterwarnings('ignore')

import numpy as np
np.set_printoptions(precision=4, suppress=True)

import matplotlib.pyplot as plt
plt.style.use(['seaborn-v0_8', 'seaborn-v0_8-whitegrid'])
get_ipython().run_line_magic("config", "InlineBackend.figure_format = 'retina'")