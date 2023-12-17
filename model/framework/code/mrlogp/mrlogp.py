from itertools import product as iterproduct
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.utils import shuffle
import numpy as np
import pandas as pd
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from tensorflow.compat.v1.keras.backend import set_session
from tensorflow.compat.v1.keras import backend as K
from tensorflow.compat.v1.keras.models import Sequential
from tensorflow.compat.v1.keras.layers import Dense
from tensorflow.compat.v1.keras.layers import Dropout
from tensorflow.compat.v1.keras.optimizers import Adam
from tensorflow.compat.v1.keras.callbacks import Callback
from tensorflow.compat.v1.keras.callbacks import ModelCheckpoint
from tensorflow.compat.v1.keras.layers import PReLU
from tensorflow.compat.v1.keras.models import load_model
from pathlib import Path
from .metrics import *
from .mrlogp_model import Model
import os
import pickle



class MRlogP():
    """
    MRlogP class, used to predict molecular logPs

    Consists of methods for generating features for training and testing from datasets 
    
    as well as for training and transfer learning models. 
    
    """   
    scaler = None
    y_class = None
    hyperparameter_options = {'droprate': [0.1], 
                              'hidden_layers': [1],
                              'hidden_nodes': [1264], 
                              'learning_rate': [0.0001],
                              'batch_size': [32], 
                              'epochs': [30],
                              }
    tl_parameter_options = {'epochs_for_output_layer': [1, 2, 3, 4, 5],
                            'epoch_for_tweaking': [1, 2, 3, 4, 5],
                            'learnrate_on_tweaking': [1.31E-5],
                            'unfrozen_layers': [2, 1],
                            'batch_size': [64, 128],
                            }
    
    def __init__(self) -> None:
        self.scaler_filename = "scaler3.pkl"  # Add a filename for saving the scaler
    
    def create_testset(self, infile_testing: str, query_mode: bool = False):
        """
        Create a MRlogP test set or the query format of compounds ready for the logP prediction.

        Parameters
        ----------
        infile_testing: (str, required)
            The path of the dataset for testing.

        query_mode: (bool, optional)
            Generate query format for compounds for logP prediction if it is True. Defaults to False.

        Returns
        -------
        It returns two arrays representing features and labels for testing.
        """
        root = os.path.dirname(os.path.abspath(__file__))
        scalar_path = os.path.abspath(os.path.join(root, "scaler3.pkl"))
        with open(scalar_path, 'rb') as scaler_file:
            self.scaler = pickle.load(scaler_file)
        print(scaler_file)

        testset = pd.read_csv(infile_testing)
        if query_mode is False:
            try:
                testset[['id', 'logP']] = testset.loc[:, "Name"].str.split(pat=';', expand=True)
            except:
                testset['logP'] = testset.loc[:, "Name"]
        else:
            testset['id'] = testset.loc[:, "Name"]

        x_ecfp4 = testset.loc[:, ["ecfp4-"+str(x) for x in range(128)]].astype('int64').astype('category').to_numpy()
        x_fp4 = testset.loc[:, ["fp4-"+str(x) for x in range(128)]].astype('int64').astype('category').to_numpy()
        x_usr = testset.loc[:, ["usrcat-"+str(x) for x in range(60)]].astype('float').to_numpy()
        cpd_name = testset.loc[:, 'Name'].astype('str').to_numpy()
        if query_mode is False:
            y = testset.loc[:, 'logP'].astype('float').to_numpy()

        x_usr = self.scaler.transform(x_usr)
        x = np.hstack([x_ecfp4, x_fp4, x_usr])
        del testset

        if query_mode is False:
            return x, y
        else:
            return x, cpd_name
    
    def predict_logp(self, query_csv_file:Path, model_path:Path):
        """
        Predict logP on query compounds using given model.    

        Parameters
        ----------
        large_dataset: (File path object, required)
            The path of the dataset for training.
        
        query_csv_file: (File path object, required)
            The path of the query compound to be predicted.

        model_path: (File path object, required)
            The path of the model used as the predictor performing logP prediction.
        """
        X_query, cpd_name_query = self.create_testset(query_csv_file, True)
        predictor = Model.load_predictor(model_path)
        result_numbers = list(predictor.predict(X_query).flatten(order='C'))
        return result_numbers
        
        

        



