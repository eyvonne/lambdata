"""
utility functions for working with dataframes

"""

import pandas as pd

TEST_DF = pd.DataFrame({'a': [1, 3, 4], 'b': [2, 5, 7]})


def genData(DF, factor):
    """DF is a dataframe to be generated off of
    factor is how many addtional rows to create"""
    df = pd.concat([DF, DF.sample(factor)])
    return df


def listCol(df, list, colName):
    """
    df is the dataframe
    list is a list to be added to the df
    colName is the name to use for the new column
    """
    ser = pd.Series(list)
    if df.shape[0] == ser.shape[0]:
        df[colName] = ser.copy()
    else:
        print('list does not have enough elements. Needs', df.shape[0])
    return df


class ManageDF:
    """
    A collection of helper functions for adding data or generating data
    All changes to the data happen inplace. 
    """
    TEST_DF = pd.DataFrame({'a': [1, 3, 4], 'b': [2, 5, 7]})

    def __init__(self, DF):
        self.df = DF

    def listCol(self, list, colName):
        """
        df is the dataframe
        list is a list to be added to the df
        colName is the name to use for the new column
        """
        ser = pd.Series(list)
        if self.df.shape[0] == ser.shape[0]:
            self.df[colName] = ser.copy()
        else:
            print('list does not have correct number of elements. Needs',
                  self.df.shape[0])
        return self.df

    def genData(self, factor):
        """DF is a dataframe to be generated off of
        factor is how many addtional rows to create"""
        self.df = pd.concat([self.df, self.df.sample(factor, replace=True)])
        return self.df
