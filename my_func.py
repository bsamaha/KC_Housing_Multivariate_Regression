import pandas as pd
import numpy as np
import seaborn as sns

import statsmodels.api as sm
from sklearn.base import BaseEstimator, RegressorMixin


def missing_data(data):
    percentage_missing = round((data.isnull().sum()/len(data))*(100),3)
    data_types = data.dtypes
    NaN_count = data.isnull().sum()
    missing_values = pd.DataFrame({'data_type': data_types,'pct_missing':percentage_missing, 'missing_count': NaN_count})
    return missing_values

def df_value_counts(df):
    for column in df:
        print('**************** Column Name:',column,'****************')
        print(df[column].value_counts())
        print('-'*100)
        print()
    return None

def log_to_dollars(number):
    dollars = np.e**number
    return dollars.round(2)

class SMWrapper(BaseEstimator, RegressorMixin):
    """ A universal sklearn-style wrapper for statsmodels regressors """
    def __init__(self, model_class, fit_intercept=True):
        self.model_class = model_class
        self.fit_intercept = fit_intercept
    def fit(self, X, y):
        if self.fit_intercept:
            X = sm.add_constant(X)
        self.model_ = self.model_class(y, X)
        self.results_ = self.model_.fit()
    def predict(self, X):
        if self.fit_intercept:
            X = sm.add_constant(X)
        return self.results_.predict(X)
