def config_display():
    import warnings
    warnings.filterwarnings('ignore')

    get_ipython().run_line_magic("reload_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")

    import numpy as np
    np.set_printoptions(precision=4, suppress=True)

    import matplotlib.pyplot as plt
    plt.rcParams['figure.constrained_layout.use'] = True
    plt.style.use(['seaborn-v0_8', 'seaborn-v0_8-whitegrid'])
    get_ipython().run_line_magic("config", "InlineBackend.figure_format = 'retina'")