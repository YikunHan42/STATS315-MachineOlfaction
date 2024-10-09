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

n_folds = 5  # Number of folds in k-fold cross-validation

clf = MolTrain(task='multilabel_classification',
               data_type='molecule',
               epochs=20,
               learning_rate=1e-4,
               batch_size=16,
               kfold=n_folds,
               save_path='./exp_5',
               metrics='auprc',
               smiles_col='nonStereoSMILES')

clf.fit('GSLF.csv')