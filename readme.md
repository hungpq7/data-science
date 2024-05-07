conda remove -y -n ds --all
conda create -y -n ds python=3.12.0 pip=24.0
conda activate ds
pip install -r requirements.txt