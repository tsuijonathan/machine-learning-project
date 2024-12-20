import pandas as pd
import numpy as np

# Data Reading

def show_data_types(df):
    """Show data types of all columns in the DataFrame."""
    print("Data Types of Columns:")
    print(df.dtypes)

def show_missing_values(df):
    """Show the number of missing values per column."""
    print("\nMissing Values in Columns:")
    print(df.isnull().sum())

def show_basic_info(df):
    """Show basic information about the DataFrame including shape, dtypes, and missing values."""
    print(f"\nDataFrame Shape: {df.shape}")
    print(f"Number of Rows: {df.shape[0]}")
    print(f"Number of Columns: {df.shape[1]}")
    print("\nData Types of Columns:")
    print(df.dtypes)
    print("\nMissing Values per Column:")
    print(df.isnull().sum())
    print("\nFirst 5 Rows of Data:")
    print(df.head())

def show_column_summary(df):
    """Show summary statistics for all columns."""
    print("\nSummary Statistics for All Columns:")
    print(df.describe(include='all'))

def show_column_values(df, column_name):
    """Show unique values for a specific column."""
    if column_name in df.columns:
        print(f"\nUnique values in column '{column_name}':")
        print(df[column_name].unique())
    else:
        print(f"Column '{column_name}' does not exist in the DataFrame.")

def show_column_value_counts(df, column_name):
    """Show value counts for a specific column."""
    if column_name in df.columns:
        print(f"\nValue counts for column '{column_name}':")
        print(df[column_name].value_counts())
    else:
        print(f"Column '{column_name}' does not exist in the DataFrame.")

def check_for_duplicates(df):
    """Check for duplicate rows in the DataFrame."""
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"\nThere are {duplicates} duplicate rows in the DataFrame.")
    else:
        print("\nNo duplicate rows found in the DataFrame.")

def show_column_info(df, column_name):
    """Show detailed information about a specific column."""
    if column_name in df.columns:
        print(f"\nColumn Info for '{column_name}':")
        print(f"Data Type: {df[column_name].dtype}")
        print(f"Number of Unique Values: {df[column_name].nunique()}")
        print(f"Number of Missing Values: {df[column_name].isnull().sum()}")
        print(f"Unique Values:")
        print(df[column_name].unique())
    else:
        print(f"Column '{column_name}' does not exist in the DataFrame.")

def show_null_percentage(df):
    """Show percentage of missing values in each column."""
    null_percentage = df.isnull().mean() * 100
    print("\nPercentage of Missing Values in Each Column:")
    print(null_percentage)


# Basic Data Cleaning

def remove_duplicates(df):
    """Remove duplicate rows from a DataFrame."""
    before_count = len(df)
    df = df.drop_duplicates()
    after_count = len(df)
    removed_count = before_count - after_count
    print(f"Removed {removed_count} duplicate rows.")
    return df

def drop_na(df, how='any', thresh=None, subset=None):
    """Drop rows with missing values (NaN) from a DataFrame."""
    return df.dropna(how=how, thresh=thresh, subset=subset)

def rename_columns(df, rename_dict):
    """Rename columns based on a dictionary."""
    return df.rename(columns=rename_dict)

def standardize_column_names(df):
    """Standardize column names (lowercase, replace spaces with underscores)."""
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def get_column_summary(df, column_name):
    """Get a summary of statistics for a specific column."""
    return df[column_name].describe()


# Data Wrangling

def convert_date_column(df, column_name):
    """
    Convert the 'flight_date' column to datetime, handling issues like extra spaces, invalid formats, and specifying the format.

    Parameters:
        df (pd.DataFrame): The DataFrame with the column to convert.
        column_name (str): The name of the column to convert.
    
    Returns:
        pd.DataFrame: DataFrame with the column converted to datetime format.
    """
    df[column_name] = df[column_name].str.strip()

    # convert using specific date format (e.g., 'dd-mm-yyyy')
    df[column_name] = pd.to_datetime(df[column_name], format='%d-%m-%Y', errors='coerce', dayfirst=True)

    return df

def convert_time_column(df, column_name):
    """
    Convert a time column (in HH:MM format or timedelta) to a string of hours and minutes only (HH:MM format).
    
    Parameters:
        df (pd.DataFrame): The DataFrame with the column to convert.
        column_name (str): The name of the column to convert.
    
    Returns:
        pd.DataFrame: DataFrame with the column converted to hours and minutes format.
    """
     # check string format
    if df[column_name].dtype == 'O':
        # Assuming the time is in HH:MM format
        df[column_name] = pd.to_datetime(df[column_name], format='%H:%M', errors='coerce').dt.strftime('%H:%M')
    
    # if column is already in timedelta format
    elif pd.api.types.is_timedelta64_dtype(df[column_name]):
        df[column_name] = df[column_name].apply(lambda x: f'{x.seconds // 3600:02}:{(x.seconds % 3600) // 60:02}')
    
    return df

