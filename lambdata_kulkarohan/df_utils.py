"""
Utility functions for working with DataFrames

Sample Data
-----------
- DF_ISNA
- DF_SPLIT
"""
# Imports
import pandas as pd 
import numpy as np 


# Sample DataFrame for isNA()
DF_ISNA = pd.DataFrame({
    "num_cars":[4, 1, 7, 2, np.nan],
    "num_houses":[1, np.nan, 3, 2, 2]
})

# Sample DataFrame for split_date()
DF_SPLIT = pd.DataFrame({'Date':['11/8/2011', '04/23/2008', '10/2/2019']})


def isNA(df):
    """ 
    Input a DataFrame and isNA(df) will return the number of NaN values.

    Use the already created DataFrame DF_ISNA to test.
    """
    print(df.isna().sum())
    return df.isna().sum()

def split_date(df):
    """ 
    Input a DataFrame with a single column of datetime values and label the
    column 'Date'. Calling split_date(df) will split the datetime values each 
    into their own column and add them to the DataFrame. 

    Use the already created DataFrame DF_SPLIT to test.
    """
    df['Year'] = pd.to_datetime(df['Date']).dt.year
    df['Month'] = pd.to_datetime(df['Date']).dt.month
    df['Day'] = pd.to_datetime(df['Date']).dt.day

    print(df)
    return df