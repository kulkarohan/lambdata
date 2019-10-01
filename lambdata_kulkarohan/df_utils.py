"""
Utility functions for working with DataFrames
"""

import pandas as pd 
from sklearn.metrics import confusion_matrix

TEST_DF = pd.DataFrame([1, 2, 3])


def isNA(a):
    return a.isna().sum(ascending=False)

def confusionMatrix(b, c):
    return confusion_matrix(b, c)
