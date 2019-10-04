"""
Utility functions for working with DataFrames
"""
import pandas as pd 
import numpy as np 


class Utils:
    """
    Utils - a class containing utilities functions for working with DataFrames

    1) import from lambdata_kulkarohan.df_utils
    2) instantiate 
    3) invoke
    """
    def isNA(self, df):
        """ 
        Input a DataFrame and isNA(df) will return the number of NaN values.

        Pass with no parameters to test with the already created DataFrame 
        DF_ISNA.
        """
        # Print the number of NaNs in each column of the DataFrame 
        print(df.isna().sum())

        # For testing purposes, return the number of NaNs in the entire DataFrame 
        sum_na = df.isna().sum().sum()
    
        return sum_na

    def split_date(self, df, column_name):
        """ 
        Input a single-column DataFrame of datetime values and input the column
        name. Calling split_date(df) will split the datetime values each 
        into their own column and add them to the DataFrame. 

        Pass with no parameters to test with the already created DataFrame
        DF_SPLIT.
        """

        # Verify that the user input for column_name is a string
        assert type(column_name) == str

        df['Year'] = pd.to_datetime(df[column_name]).dt.year
        df['Month'] = pd.to_datetime(df[column_name]).dt.month
        df['Day'] = pd.to_datetime(df[column_name]).dt.day
        
        # Print the DataFrame with the newly added columns
        print(df)

        # For testing purposes, return the number of columns
        # If the number is anything other than 4, the function did not work
        num_columns = len(df.columns)

        return num_columns

if __name__ == "__main__":
    util = Utils()

    util.isNA()
    util.split_date()
