---
title: Data Science with Python
---

# Data Science
A Data Science book. Powered by [Jupyter Book](https://jupyterbook.org).


## Local build
```bash
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
      "scale": "80%",
      "align": "center"
     }
    }
```

## Image
```
:::{image} ../image/chap_05/matplotlib_color_names.svg
:height: 600px
:align: center
:::
```

:::{image} ../image/chap_05/matplotlib_color_names.svg
:height: 600px
:align: center
:::

## Topic
```text
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
:::{note}
Attention is all you need.
:::
```text
:::{note}
Attention is all you need.
:::
```
::::

::::{tab-item} Example
:::{admonition} Example
:class: tip
Attention is all you need.
:::
```text
:::{admonition} Example
:class: tip
Attention is all you need.
:::
```
::::

::::{tab-item} Pitfall
:::{admonition} Pitfall
:class: tip
Attention is all you need.
:::
```text
:::{admonition} Pitfall
:class: tip
Attention is all you need.
:::
```
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
```text
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
flowchart TB
  SGD(((SGD)))
  Momentum(Momentum)
  AdaGrad(AdaGrad)
  Nesterov(Nesterov)
  RMSProp(RMSProp)
  AdaDelta(AdaDelta)
  Adam(((Adam)))
  Nadam(Nadam)
  AMSGrad(AMSGrad)
  AdaMax(AdaMax)
  AdamW(AdamW)

  SGD -- adaptive<br>gradient --> Momentum
  SGD -- adaptive<br>learning rate --> AdaGrad

  Momentum --> Nesterov
  Momentum --> Adam
  Nesterov --> Nadam

  AdaGrad --> RMSProp
  AdaGrad --> AdaDelta
  RMSProp --> Adam

  Adam --> Nadam
  Adam --> AMSGrad
  Adam --> AdaMax
  Adam --> AdamW
:::
```

:::{mermaid}
:align: center
flowchart TB
  SGD(((SGD)))
  Momentum(Momentum)
  AdaGrad(AdaGrad)
  Nesterov(Nesterov)
  RMSProp(RMSProp)
  AdaDelta(AdaDelta)
  Adam(((Adam)))
  Nadam(Nadam)
  AMSGrad(AMSGrad)
  AdaMax(AdaMax)
  AdamW(AdamW)

  SGD -- adaptive<br>gradient --> Momentum
  SGD -- adaptive<br>learning rate --> AdaGrad

  Momentum --> Nesterov
  Momentum --> Adam
  Nesterov --> Nadam

  AdaGrad --> RMSProp
  AdaGrad --> AdaDelta
  RMSProp --> Adam

  Adam --> Nadam
  Adam --> AMSGrad
  Adam --> AdaMax
  Adam --> AdamW
:::

Incoming topics:
- Data Structure and Algorithms
- Optimization
- Network Analysis
- Polars library
- Bokeh library
- FastAPI library
- Association Rules
- Image Processing
- Convolutional Network
- Transfer Learning
- Streamlit and Gradio
- Langchain and Langgraph
- Statistics in R

