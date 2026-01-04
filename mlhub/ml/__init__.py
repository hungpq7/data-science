import yaml
import importlib
from pathlib import Path

with Path(__file__).with_name('ml_alias.yaml').open('r', encoding='utf-8') as f:
    _lazy = yaml.safe_load(f)

def __getattr__(name):
    if name in _lazy:
        target = _lazy[name]

        # Split into "module" and "attribute"
        module_name, _, attr = target.rpartition(".")
        if not module_name:  # case: whole module (e.g., "numpy")
            module_name, attr = target, None

        mod = importlib.import_module(module_name)
        obj = getattr(mod, attr) if attr else mod

        globals()[name] = obj
        return obj

    raise AttributeError(f"module {__name__} has no attribute {name}")