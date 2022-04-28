import pandas as pd
import janitor
import pandas_flavor as pf

@pf.register_dataframe_method
def calc_diff(df, col1, col2, new_col):
    """
    Calculates simple row-wise difference between the values of two columns. Helpful when trying to discover discrepancies in two methods of calculation or two sources of data.
    Parameters
    ----------
    df : the dataframe containing the columns you want to use
        
    col1 : string indicating the name of the first column to use in the difference calculation
        
    col2 : string indicating the name of the second column to use in the difference calculation
        
    new_col : string indicating the name to assign to the new, difference column
        

    Returns
    -------
    Dataframe containing all columns passed to it along with a new column that contains the difference calculation
    """
    df[new_col] = df[col1] - df[col2]
    return df

@pf.register_dataframe_method
def check_missing(df):
    """
    Gives a count and percentage for each column of a data frame indicating the amount of the column that is not null
    
    Parameters
    ----------
    df : data frame that you want to check 
        

    Returns
    -------

    A data frame with a row for each column of the input data frame and 3 columns. Column names are column_name, not_null_count, and not_null_percentage
    """
    total_rows = df.shape[0]
    df = df.notna().sum().reset_index().rename_columns({'index': 'column_name', 0: 'not_null_count'})
    df['not_null_percentage'] = round((df.not_null_count / total_rows) * 100, 2)
    return df