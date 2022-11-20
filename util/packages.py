# general python
import os
import glob
import logging
import warnings
import datetime as dt
import dateutil.relativedelta as du
import re
from sspipe import p, px

# general data science
import numpy as np
import pandas as pd
import janitor
import scipy import stats
import numpy.random as rd
import sympy as sym

# visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# general machine learning
from sklearn.pipeline import make_pipeline

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler, Normalizer, StandardScaler
from feature_engine.transformation import BoxCoxTransformer, YeoJohnsonTransformer

# machine learning algorithms
from xgboost import XGBClassifier, XGBRegressor
from lightgbm import LGBMClassifier, LGBMRegressor
from catboost import CatBoostClassifier, CatBoostRegressor

# time series analysis
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
import ruptures as rpt

# time series forecast


# text mining
import nltk
import spacy

# config
np.set_printoptions(precision=4, suppress=True)
pd.options.display.float_format = '{:,.2f}'.format
pd.options.display.max_colwidth = 1000
pd.options.display.max_columns = 500
pd.options.display.max_rows = 1000
plt.style.use(['seaborn', 'seaborn-whitegrid'])
