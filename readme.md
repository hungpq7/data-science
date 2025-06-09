# Data Science
[![NBViewer](https://img.shields.io/badge/Render-nbviewer-orange?logo=github)](https://nbviewer.jupyter.org/github/hungpq7/data-science/tree/main/)
[![MyBinder](https://img.shields.io/badge/Render-mybinder-indianred?logo=github)](https://mybinder.org/v2/gh/hungpq7/data-science/main)
[![Datalore](https://img.shields.io/badge/Open-datalore-teal?logo=python)](https://datalore.jetbrains.com/HICh9tMzg84aKmizzLSzaz/UQKR2rXCbGCaktk3s2qXou/notebooks)
[![GoogleColab](https://img.shields.io/badge/Open-google%20colab-goldenrod?logo=python)](https://drive.google.com/drive/folders/1Rm4c_0G4R7Cyopcenzx7-EnCt3bR4HL7)

Mathematics &bull; Data Manipulation &bull; Data Visualization &bull; Machine Learning &bull; Deep Learning


[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f)](https://www.python.org/)
[![Made with Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f)](http://commonmark.org)
[![Made with LaTex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)

### Command line
```python
conda activate base
conda remove -y -n ds --all
conda create -y -n ds python=3.10.0 pip=24.0
conda activate ds
pip install -r requirements.txt

conda create --name ds-optimize --clone ds
```

### HTML
```html
<code style="font-size:13px"></code>
<img src="../image/chap-09/.png" style="height:300px; margin:20px auto 20px;">

&#9800;&nbsp;<b>Tip</b><br>
&#9800;&nbsp;<b>Note</b><br>
&#9800;&nbsp;<b>Practice</b><br>

---
*&#9829; By Quang Hung x Thuy Linh &#9829;*
```

### Python imports
```python
import sys; sys.path.append('..')
from dsutil import np, pd, plt, sns, ml, stats
```

Force update URLs
- NBViewer: `?flush_cache=true`
- Github: `?token=$(date +%s)`
