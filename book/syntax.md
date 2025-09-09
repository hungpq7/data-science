### Insert image
```
:::{image} ../image/GRADIENT.png
:height: 350px
:align: center
:::
```

### Grey block
```
:::{topic} TITLE
CONTENT
:::
```

### Admonition
Selected classes:
- tip (green)
- note (blue)
- attention (orange)
- danger (red)

```
:::{attention}
CONTENT
:::
```

```
:::{admonition} TITLE
:class: attention
CONTENT
:::
```

### Cell tags
```

```

### Local build
```
rm -rf _build
jb build . --config book/config.yml --toc book/toc.yml
```