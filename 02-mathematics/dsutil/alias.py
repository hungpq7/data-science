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
        module, attr = _lazy[name]
        mod = importlib.import_module(module)

        if name == "pd":
            try:
                import janitor 
            except ImportError:
                pass

        globals()[name] = mod if attr is None else getattr(mod, attr)
        return globals()[name]
    raise AttributeError(f"module {__name__} has no attribute {name}")
