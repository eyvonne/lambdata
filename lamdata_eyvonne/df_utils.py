"""
utility functions for working with dataframes

"""

import pandas as pd

TEST_DF = pd.DataFrame([1,3,4])

def genData (DF, factor):
    """
    DF is a dataframe to be generated off of
    factor is how many addtional rows to create
    """
    df=pd.concat([DF, DF.sample(factor)])
    return df

def listCol(df, list, colName):
    """
    df is the dataframe
    list is a list to be added to the df
    colName is the name to use for the new column
    """
    ser=pd.Series(list)
    if df.shape[0]==ser.shape[0]:
        df[colName]=ser.copy()
    else:
        print('list does not have enough elements. Needs', df.shape[0])
    return df
