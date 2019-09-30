"""
Utility functions for working with DataFrames
"""

import pandas as pd 
from sklearn.metrics import confusion_matrix

TEST_DF = pd.DataFrame([1, 2, 3])

isna = pd.isna()
confusion_matrix = confusion_matrix()
