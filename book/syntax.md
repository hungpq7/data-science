### Insert image
```
:::{image} ../image/gradient.png
:height: 350px
:align: center
:::
```

### Grey block
```
:::{topic} This is topic title
This is topic content
:::
```

### Admonition
```
tip       : green
note      : blue
attention : orange
danger    : red

:::{attention}
:::

:::{admonition}
:class: attention
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