
import pandas as pd
import numpy as np
import re

import sys
sys.path.append('utils')  # Add the directory containing functions.py
import functions

# reat dataframes
clean_df = pd.read_csv('data/raw/Clean_Dataset.csv')
business_df = pd.read_csv('data/raw/business.csv')
economy_df = pd.read_csv('data/raw/economy.csv')


# display basic information
functions.show_basic_info(clean_df)
functions.show_basic_info(business_df)
functions.show_basic_info(economy_df)

# drop duplicate index column
clean_df.drop(columns=['Unnamed: 0'], inplace=True)

# rename columns in clean_df
replacement_dict = {
    'airline': 'airline_name',
    'flight':'flight_code',
    'source_city': 'departure_city',
    'duration': 'flight_duration',
    'destination_city': 'arrival_city',
    'duration':'flight_duration',
    'price': 'price'
}

clean_df = functions.rename_columns(clean_df, replacement_dict)
clean_df.head()

# rename columns in business_df
replacement_dict = {
    'date': 'flight_date',
    'airline': 'airline_name',
    'ch_code': 'airline_code',
    'num_code': 'flight_number',
    'dep_time': 'departure_time',
    'from': 'departure_city',
    'time_taken': 'flight_duration',
    'stop': 'stops',
    'arr_time': 'arrival_time',
    'to': 'arrival_city',
    'price': 'price'
}

business_df = functions.rename_columns(business_df, replacement_dict)
business_df.head()

# rename columns in economy_df
replacement_dict = {
    'date': 'flight_date',
    'airline': 'airline_name',
    'ch_code': 'airline_code',
    'num_code': 'flight_number',
    'dep_time': 'departure_time',
    'from': 'departure_city',
    'time_taken': 'flight_duration',
    'stop': 'stops',
    'arr_time': 'arrival_time',
    'to': 'arrival_city',
    'price': 'price'
}

economy_df = functions.rename_columns(economy_df, replacement_dict)
economy_df.head()

# remove duplicate rows
functions.remove_duplicates(clean_df)
functions.remove_duplicates(business_df)
functions.remove_duplicates(economy_df)

# Data Standardization
# - Ensuring matching data types
# - Formatting values consistently
# - Normalizing textual data

# convert 'price' column to integer
def standardize_price(df, column_name='price'):
    df[column_name] = df[column_name].str.replace(',', '', regex=True).astype(int)
    return df

business_df = standardize_price(business_df, 'price')
economy_df = standardize_price(economy_df, 'price')

print('Business DF:')
print(business_df)
print('\nEconomy DF:')
print(economy_df)


# convert 'stops' column values to integers [0, 1, 2]

# clean_df
stop_mapping = {
        'zero': 0,
        'one': 1,
        'two_or_more': 2
    }
    
clean_df['stops'] = clean_df['stops'].map(stop_mapping)

# business_df and economy_df
def stops_to_integers(df, column_name='stops'):
    def map_stops(value):
        if 'non-stop' in value:
            return 0
        else:
            match = re.search(r'\d+', value) # extract first digit w regex
            return int(match.group()) if match else None

    df[column_name] = df[column_name].apply(map_stops)
    return df

stops_to_integers(business_df)
stops_to_integers(economy_df)

# date formatting
functions.convert_date_column(economy_df, 'flight_date')
functions.convert_date_column(business_df, 'flight_date')

# time formatting
functions.convert_time_column(business_df, 'arrival_time')
functions.convert_time_column(business_df, 'departure_time')
functions.convert_time_column(economy_df, 'arrival_time')
functions.convert_time_column(economy_df, 'departure_time')

# generate flight codes
def create_flight_code(df):
    df['flight_code'] = df['airline_code'] + '-' + df['flight_number'].astype(str)
    return df

create_flight_code(business_df)
create_flight_code(economy_df)

# drop columns
business_df = business_df.drop(columns=['airline_code', 'flight_number'])
economy_df = economy_df.drop(columns=['airline_code', 'flight_number'])

# generate flight time groups ['Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late Night']
def categorize_flight_time(time_str):
    hour = int(time_str.split(':')[0]) 
    
    # categorize based on the hour block
    if 4 <= hour < 6:
        return 'Early Morning'
    elif 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 21:
        return 'Evening'
    elif 21 <= hour < 24:
        return 'Night'
    else:
        return 'Late Night'
    

# implementation
business_df['departure_time_group'] = business_df['departure_time'].apply(categorize_flight_time)
business_df['arrival_time_group'] = business_df['arrival_time'].apply(categorize_flight_time)

economy_df['departure_time_group'] = economy_df['departure_time'].apply(categorize_flight_time)
economy_df['arrival_time_group'] = economy_df['arrival_time'].apply(categorize_flight_time)

# clean time group columns
clean_df.rename(columns={'departure_time': 'departure_time_group', 'arrival_time' : 'arrival_time_group'}, inplace=True)
columns_to_clean = ['departure_time_group', 'arrival_time_group']

for col in columns_to_clean:
    clean_df[col] = clean_df[col].str.replace(' ', '', regex=True).str.replace('_', ' ', regex=True)


# standardize airline names across dataframes
def standardize_airline_names(df, column_name='airline_name'):
    standard_name_mapping = {
        'SpiceJet': 'SpiceJet',
        'AirAsia': 'Air Asia',
        'Vistara': 'Vistara',
        'GO_FIRST': 'Go First',
        'GO FIRST': 'Go First',
        'Indigo': 'Indigo',
        'Air_India': 'Air India',
        'Air India': 'Air India',
        'Trujet': 'TruJet',
        'StarAir': 'Star Air',
    }
    
    df[column_name] = df[column_name].replace(standard_name_mapping)
    return df

# implementation
clean_df = standardize_airline_names(clean_df)
print(clean_df['airline_name'].unique())

business_df = standardize_airline_names(business_df)
print(clean_df['airline_name'].unique())

economy_df = standardize_airline_names(economy_df)
print(economy_df['airline_name'].unique())

# Format 'flight_duration' column to minutes
def convert_duration_to_minutes(df, column_name):
    df[column_name] = (df[column_name] * 60).round().astype(int)
    return df

clean_df = convert_duration_to_minutes(clean_df, 'flight_duration')

# format function handling different formats and dot notation indicating days
def convert_duration_string_to_minutes(duration_str):
    hours, minutes = 0, 0
    
    if '1.' in duration_str: # extract days
        hours = 24 
        duration_str = duration_str.replace('1.', '')

    if 'h' in duration_str: # extract hours
        hours += int(duration_str.split('h')[0])

    if 'm' in duration_str: # extract minutes
        try:
            minutes_str = duration_str.split('h ')[1].split('m')[0]  # extract minutes portion after 'h'
            minutes = int(minutes_str) if minutes_str else 0  # set minutes to 0 if empty
        except IndexError:
            minutes = 0  # if no value after 'h'
    
    return int(hours * 60 + minutes) # return total in minutes


business_df['flight_duration'] = business_df['flight_duration'].apply(convert_duration_string_to_minutes)
economy_df['flight_duration'] = economy_df['flight_duration'].apply(convert_duration_string_to_minutes)

# reorder columns
def reorder_columns(df, column_order):
    df = df[column_order]
    return df

column_order = [
    'flight_date', 'airline_name', 'flight_code', 
    'departure_time', 'departure_city', 
    'arrival_time', 'arrival_city', 
    'flight_duration', 'stops', 'price', 
    'departure_time_group', 'arrival_time_group'
]

business_df = reorder_columns(business_df, column_order)
economy_df = reorder_columns(economy_df, column_order)

clean_df = clean_df[[
    'airline_name', 'flight_code', 
    'departure_city', 
    'arrival_city', 
    'flight_duration', 'stops', 'price', 'class', 'days_left',
    'departure_time_group', 'arrival_time_group'
]]

# check modified dfs
clean_df.head()
business_df.head()
economy_df.head()

# Export Data Frames to .csv
# clean_df.to_csv('../../data/clean/clean_dataset_df.csv', index=False)
# business_df.to_csv('../../data/clean/clean_business_df.csv', index=False)
# economy_df.to_csv('../../data/clean/clean_economy_df.csv', index=False)
