import pandas as pd
import seaborn as sns


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
    dollars = 10**number
    return dollars.round(2)

