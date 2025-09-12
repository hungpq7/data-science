import warnings
warnings.filterwarnings('ignore')

import importlib

_lazy = dict(
    os = "os",
    sys = "sys",
    re = "re",
    dt = "datetime",
    du = "dateutil.relativedelta",

    np = "numpy",
    pd = "pandas",
    stats = "scipy.stats",
    linalg = "scipy.linalg",
    optimize = "scipy.optimize",
    sym = "sympy",
    plt = "matplotlib.pyplot",
    sns = "seaborn",
    nx = "networkx",
    skl = "sklearn",
)


def __getattr__(name):
    if name in _lazy:
        module = _lazy[name]
        mod = importlib.import_module(module)

        if name == "np":
            mod.set_printoptions(precision=4, suppress=True)

        elif name == "plt":
            mod.rcParams['figure.constrained_layout.use'] = True
            mod.style.use(['seaborn-v0_8', 'seaborn-v0_8-whitegrid'])
            try:
                ip = get_ipython()
                ip.run_line_magic("config", "InlineBackend.figure_format = 'retina'")
            except Exception:
                pass

        elif name == "pd":
            try:
                import janitor
            except ImportError:
                pass

        globals()[name] = mod
        return mod

    raise AttributeError(f"module {__name__} has no attribute {name}")

def setup_timezone():
    import os
    import time
    os.environ['TZ'] = 'Asia/Ho_Chi_Minh'
    time.tzset()

def setup_reload():
    get_ipython().run_line_magic("reload_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")