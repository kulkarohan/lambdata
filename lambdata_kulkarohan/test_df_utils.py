import unittest
import pandas as pd 
import numpy as np 

import df_utils as dfu 

class TestDfUtils(unittest.TestCase):
    """
    Test the utlity helper functions from df_utils.py
    """
    def test_isNA(self):
        """
        Test the isNA method by verifying the total number NaN values in a 
        sample DataFrame 
        """
        # Sample DataFrame for isNA()
        DF_ISNA = pd.DataFrame({
            "num_cars":[4, 1, 7, 2, np.nan],
            "num_houses":[1, np.nan, 3, 2, 2]
        })
        self.utils = dfu.Utils()
        self.assertEqual(self.utils.isNA(DF_ISNA), 2)
       
    def test_split_date(self):
        """
        Test the split_date method by verifying that the returned
        DataFrame has 4 columns (original + year, month, day). If the 
        result is anything other than 4, it is not valuable.
        """
        # Sample DataFrame for split_date()
        DF_SPLIT = pd.DataFrame({
            'Date':['11/8/2011', '04/23/2008', '10/2/2019']
        })

        self.utils = dfu.Utils()
        self.assertEqual(self.utils.split_date(DF_SPLIT, 'Date'), 4)

if __name__ == '__main__':
    unittest.main()
