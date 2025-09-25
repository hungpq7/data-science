import warnings
warnings.filterwarnings('ignore')

import importlib

_lazy = dict(
    os = 'os',
    sys = 'sys',
    re = 're',
    dt = 'datetime',
    du = 'dateutil.relativedelta',

    np = 'numpy',
    pd = 'pandas',
    stats = 'scipy.stats',
    linalg = 'scipy.linalg',
    optimize = 'scipy.optimize',
    pg = 'pingouin',
    sym = 'sympy',
    mpl = 'matplotlib',
    plt = 'matplotlib.pyplot',
    sns = 'seaborn',
    px = 'plotly.express',
    nx = 'networkx',
    skl = 'sklearn',
    metrics = 'sklearn.metrics',
    pl = 'polars',
    fe = 'feature_engine',
)

def lazy_getattr(name):
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