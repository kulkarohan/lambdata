"""
Utility functions for working with DataFrames
"""

import pandas as pd 
from sklearn.metrics import confusion_matrix

TEST_DF = pd.DataFrame([1, 2, 3])


def ISNA(obj):
    return pd.isna(obj)

def CONFUSION_MATRIX(obj):
    return confusion_matrix(obj)
