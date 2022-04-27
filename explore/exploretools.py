import pandas as pd
import janitor
import pandas_flavor as pf

@pf.register_dataframe_method
def calc_diff(df, col1, col2, new_col):
    df[new_col] = df[col1] - df[col2]
    return df

