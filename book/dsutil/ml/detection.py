from feature_engine.outliers import Winsorizer as WinsorizerDetector
from pyod.models.iforest import IForest as IsolationForestDetector
from pyod.models.knn import KNN as KNNDetector
from pyod.models.lof import LOF as LOFDetector
from pyod.models.ecod import ECOD as EmpiricalCDFDetector
from pyod.models.copod import COPOD as CopulaBasedDetector