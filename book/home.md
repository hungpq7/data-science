---
title: Data Science with Python
---

# Data Science
A Data Science book. Powered by [Jupyter Book](https://jupyterbook.org).

## Local build
```
rm -rf _build
jb build . --config book/config.yml --toc book/toc.yml
```

## Hyperlinks
```
- [Jupyter Book](https://jupyterbook.org)
- [`langchain`](https://www.langchain.com/)
```

- [Jupyter Book](https://jupyterbook.org)
- [`langchain`](https://www.langchain.com/)

## Cell tags
```
scroll-output
hide-cell
hide-input
hide-output
remove-cell
remove-input
remove-output
```

## Cell metadata
Using [MyST-NB](https://myst-nb.readthedocs.io/en/latest/configuration.html#cell-level-configuration)
```json
    "mystnb": {
     "image": {
      "align": "center",
      "scale": "70%"
     }
    },
```

## Image
```
:::{image} ../image/chap_06/svm_hard.png
:height: 350px
:align: center
:::
```

:::{image} ../image/chap_06/svm_hard.png
:height: 350px
:align: center
:::

## Topic
```txt
:::{topic} Title
Content
:::
```

:::{topic} Title
Content
:::

## Callout
With [Sphinx](https://sphinx-book-theme.readthedocs.io/en/stable/reference/kitchen-sink/admonitions.html)
- `tip` (green)
- `note` (blue)
- `attention` (orange)
- `danger` (red)

:::::{tab-set}
::::{tab-item} Note
```txt
:::{note}
Attention is all you need.
:::
```
:::{note}
Attention is all you need.
:::
::::

::::{tab-item} Practice
```txt
:::{admonition} Practice
:class: tip
Attention is all you need.
:::
```
:::{admonition} Practice
:class: tip
Attention is all you need.
:::
::::
:::::

## Dropdown
```
:::{dropdown} Click to reveal!
Something hidden!
:::
```

:::{dropdown} Click to reveal!
Something hidden!
:::

## Admonition
General concept of image, dropdown, callout,...
```txt
:::{admonition} Transformer
:class: tip, toggle
Attention is all you need.
:::
```

:::{admonition} Transformer
:class: tip, toggle
Attention is all you need.
:::

## Tab content
````
::::{tab-set}
:::{tab-item} XGBoost
```python
from xgboost import XGBClassifier, XGBRegressor
```
:::
:::{tab-item} LightGBM
```python
from lightgbm import LGBMClassifier, LGBMRegressor
```
:::
:::{tab-item} CatBoost
```python
from catboost import CatBoostClassifier, CatBoostRegressor
```
:::
::::
````

::::{tab-set}
:::{tab-item} XGBoost
```python
from xgboost import XGBClassifier, XGBRegressor
```
:::
:::{tab-item} LightGBM
```python
from lightgbm import LGBMClassifier, LGBMRegressor
```
:::
:::{tab-item} CatBoost
```python
from catboost import CatBoostClassifier, CatBoostRegressor
```
:::
::::

## Diagram
With [Mermaid](https://mermaid.js.org/)

```
:::{mermaid}
:align: center
sequenceDiagram
    Alice ->> John: Hello John, how are you?
    John -->> Alice: Great!
    Alice -) John: See you later!
:::
```

:::{mermaid}
:align: center
sequenceDiagram
    Alice ->> John: Hello John, how are you?
    John -->> Alice: Great!
    Alice -) John: See you later!
:::