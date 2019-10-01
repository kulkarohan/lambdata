"""
Utility functions for working with DataFrames
"""

import pandas as pd 

TEST_DF = pd.DataFrame([1, 2, 3])

# Check DataFrame for nulls
def isNA(a):
    return a.isna().sum(ascending=False)

# Split date into multiple columns
def split_date(df):
    df = df.copy()

    df['Year'] = df.dt.year
    df['Month'] = df.dt.month
    df['Day'] = df.dt.day

    return df
