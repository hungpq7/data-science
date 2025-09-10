---
title: Data Science with Python
---

# Data Science
A Data Science book. Powered by [Jupyter Book](https://jupyterbook.org){:target="_blank"}.

<a href="https://jupyterbook.org" target="_blank">Hello, world!</a>

## Local build
```
rm -rf _build
jb build . --config book/config.yml --toc book/toc.yml
```

## Cell tags
```

```

## Image
```
:::{image} ../image/chap-06/svm-hard.png
:height: 350px
:align: center
:::
```

:::{image} ../image/chap-06/svm-hard.png
:height: 350px
:align: center
:::

## Topic
```
:::{topic} TITLE
CONTENT
:::
```

:::{topic} TITLE
CONTENT
:::

## Callout
With [Sphinx](https://sphinx-book-theme.readthedocs.io/en/stable/reference/kitchen-sink/admonitions.html)
- `tip` (green)
- `note` (blue)
- `attention` (orange)
- `danger` (red)

```
:::{note}
Attention is all you need.
:::
```

:::{note}
Attention is all you need.
:::

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
```
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