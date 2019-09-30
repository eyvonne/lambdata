"""
a collection of helper functions for DS
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

ONES=pd.DataFrame(np.ones(10))
ZEROS=pd.DataFrame(np.zeros(15))


def traintest(df, df2):
    train, test, tar, tartest=train_test_split(df, df2)
    return tar
