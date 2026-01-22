from .setup import NBConfig
NBConfig.setup()

import yaml
import importlib
from pathlib import Path

from . import ml

p = Path(__file__).parent.resolve() / 'alias/ds_module.yaml'
with p.open('r', encoding='utf-8') as f:
    _lazy = yaml.safe_load(f)

def __getattr__(name):
    if name in _lazy:
        module = importlib.import_module(_lazy[name])

        if name == 'np':
            module.set_printoptions(precision=4, suppress=True)

        elif name == 'plt':
            module.rcParams['figure.constrained_layout.use'] = True
            module.style.use(['seaborn-v0_8', 'seaborn-v0_8-whitegrid'])
            try:
                ip = get_ipython()
                ip.run_line_magic("config", "InlineBackend.figure_format = 'retina'")
            except Exception:
                pass

        elif name == 'pd':
            try:
                import janitor
            except ImportError:
                pass

        globals()[name] = module
        return module

    raise AttributeError(f'module {__name__} has no attribute {name}')