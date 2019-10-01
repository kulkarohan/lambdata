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


class Utils:
    """
    Utils - a class containing utilities functions for working with DataFrames

    1) import from lambdata_kulkarohan.df_utils
    2) instantiate 
    3) invoke
    """
    def __init__(self):
        pass
        
    def isNA(self, df=DF_ISNA):
        """ 
        Input a DataFrame and isNA(df) will return the number of NaN values.

        Pass with no parameters to test with the already created DataFrame 
        DF_ISNA.
        """
        print(df.isna().sum())
        return df.isna().sum()

    def split_date(self, df=DF_SPLIT):
        """ 
        Input a DataFrame with a single column of datetime values and label the
        column 'Date'. Calling split_date(df) will split the datetime values each 
        into their own column and add them to the DataFrame. 

        Pass with no parameters to test with the already created DataFrame
        DF_SPLIT.
        """
        df['Year'] = pd.to_datetime(df['Date']).dt.year
        df['Month'] = pd.to_datetime(df['Date']).dt.month
        df['Day'] = pd.to_datetime(df['Date']).dt.day

        print(df)
        return df