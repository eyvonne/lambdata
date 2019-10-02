"""
a collection of helper functions for DS
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(15))
MOREONES = pd.DataFrame(np.ones(50))
TEST_DF = pd.DataFrame({'a': [1, 3, 4], 'b': [2, 5, 7]})

# this was proof of concept that I could use sklearn


def traintest(df, df2):
    train, test, tar, tartest = train_test_split(df, df2)
    return tar
