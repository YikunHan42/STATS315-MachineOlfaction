import os
import numpy as np
import pandas as pd
from unimol_tools import MolPredict
from unimol_tools.data import DataHub
from unimol_tools.models import NNModel
from unimol_tools.tasks import Trainer
from unimol_tools.utils import YamlHandler
from unimol_tools.utils import logger
from unimol_tools.tasks.split import Splitter
from sklearn.model_selection import KFold
from unimol_tools import MolTrain
import joblib

clf = MolPredict(load_model='./exp_5')

res = clf.predict(data='test_set_42_stratified.csv', save_path='./save')