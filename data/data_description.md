# Data Description

This document provides an overview of the contents of the `data` folder.

## Folder Structure
The `data` folder contains the following subdirectories and files:

- `raw/`: Contains the raw, unprocessed data files.
  - `Clean_Dataset.csv`: A cleaned version of the dataset with missing values handled and outliers removed.
  - `business.csv`: The original, unprocessed data.
  - `economy.csv`

- `clean/`: Contains the processed data files ready for use in model training or analysis.
  - `clean_dataset_df.csv`
  - `clean_business_df.csv`
  - `clean_economy_df.csv`
  - `clean_combined.csv`: Dataframe combining the three initial ones.


## Data Cleaning & Transformation
(tbd)


## DataFrame Details

## `clean_dataset_df.csv`

This dataset contains detailed information about flights, including the airline, flight schedule, duration, price, and other relevant flight details. It has been preprocessed and cleaned to be ready for analysis.

#### DataFrame Shape:
- **Number of Rows**: 300,153
- **Number of Columns**: 11

#### Columns:
1. **`airline_name`**: The name of the airline operating the flight (e.g., "SpiceJet").
2. **`flight_code`**: The unique code assigned to each flight (e.g., "SG-8709").
3. **`departure_city`**: The city from which the flight departs (e.g., "Delhi").
4. **`arrival_city`**: The city where the flight arrives (e.g., "Mumbai").
5. **`flight_duration`**: The duration of the flight in minutes (e.g., `130` minutes).
6. **`stops`**: The number of stops made by the flight (e.g., `0` for non-stop flights).
7. **`price`**: The price of the flight in Indian Rupees (INR) (e.g., `5953`).
8. **`class`**: The class of the flight (e.g., "Economy").
9. **`days_left`**: The number of days remaining until the flight date (e.g., `1`).
10. **`departure_time_group`**: The time group in which the flight departs, categorized into various time slots (e.g., "Evening", "Morning").
11. **`arrival_time_group`**: The time group in which the flight arrives at its destination (e.g., "Night", "Morning").

#### Data Types of Columns:
- **`airline_name`**: object
- **`flight_code`**: object
- **`departure_city`**: object
- **`arrival_city`**: object
- **`flight_duration`**: int64
- **`stops`**: int64
- **`price`**: int64
- **`class`**: object
- **`days_left`**: int64
- **`departure_time_group`**: object
- **`arrival_time_group`**: object


## `clean_business_df.csv`

This dataset contains information about business class flights, including the flight details, departure and arrival times, duration, price, and more. It has been preprocessed and cleaned to be used in further analysis.

#### DataFrame Shape:
- **Number of Rows**: 93,487
- **Number of Columns**: 12

#### Columns:
1. **`flight_date`**: The date on which the flight departs (e.g., "2022-02-11").
2. **`airline_name`**: The name of the airline operating the flight (e.g., "Air India").
3. **`flight_code`**: The unique code assigned to each flight (e.g., "AI-868").
4. **`departure_time`**: The time of departure (e.g., "18:00").
5. **`departure_city`**: The city from which the flight departs (e.g., "Delhi").
6. **`arrival_time`**: The time of arrival at the destination (e.g., "20:00").
7. **`arrival_city`**: The city where the flight arrives (e.g., "Mumbai").
8. **`flight_duration`**: The duration of the flight in minutes (e.g., `120` minutes).
9. **`stops`**: The number of stops made by the flight (e.g., `0` for non-stop flights).
10. **`price`**: The price of the flight (e.g., `25612`).
11. **`departure_time_group`**: The time group for departure (e.g., "Evening").
12. **`arrival_time_group`**: The time group for arrival (e.g., "Evening").

#### Data Types of Columns:
- `flight_date`: datetime64[ns]
- `airline_name`: object
- `flight_code`: object
- `departure_time`: object
- `departure_city`: object
- `arrival_time`: object
- `arrival_city`: object
- `flight_duration`: int64
- `stops`: int64
- `price`: int64
- `departure_time_group`: object
- `arrival_time_group`: object

#### Missing Values per Column:
- No missing values in any of the columns.


#### DataFrame Shape:
- **Number of Rows**: 206,774
- **Number of Columns**: 12

#### Columns:
1. **`flight_date`**: The date on which the flight departs (e.g., "2022-02-11").
2. **`airline_name`**: The name of the airline operating the flight (e.g., "SpiceJet").
3. **`flight_code`**: The unique code assigned to each flight (e.g., "SG-8709").
4. **`departure_time`**: The time of departure (e.g., "18:55").
5. **`departure_city`**: The city from which the flight departs (e.g., "Delhi").
6. **`arrival_time`**: The time of arrival at the destination (e.g., "21:05").
7. **`arrival_city`**: The city where the flight arrives (e.g., "Mumbai").
8. **`flight_duration`**: The duration of the flight in minutes (e.g., `130` minutes).
9. **`stops`**: The number of stops made by the flight (e.g., `0` for non-stop flights).
10. **`price`**: The price of the flight (e.g., `5953`).
11. **`departure_time_group`**: The time group for departure (e.g., "Evening").
12. **`arrival_time_group`**: The time group for arrival (e.g., "Night").

#### Data Types of Columns:
- `flight_date`: datetime64[ns]
- `airline_name`: object
- `flight_code`: object
- `departure_time`: object
- `departure_city`: object
- `arrival_time`: object
- `arrival_city`: object
- `flight_duration`: int64
- `stops`: int64
- `price`: int64
- `departure_time_group`: object
- `arrival_time_group`: object

#### Missing Values per Column:
- No missing values in any of the columns.


## `clean_economy_df.csv`

This dataset contains information about economy class flights, including the flight details, departure and arrival times, duration, price, and more. It has been preprocessed and cleaned to be used in further analysis.

#### DataFrame Shape:
- **Number of Rows**: 206,774
- **Number of Columns**: 12

#### Columns:
1. **`flight_date`**: The date on which the flight departs (e.g., "2022-02-11").
2. **`airline_name`**: The name of the airline operating the flight (e.g., "SpiceJet").
3. **`flight_code`**: The unique code assigned to each flight (e.g., "SG-8709").
4. **`departure_time`**: The time of departure (e.g., "18:55").
5. **`departure_city`**: The city from which the flight departs (e.g., "Delhi").
6. **`arrival_time`**: The time of arrival at the destination (e.g., "21:05").
7. **`arrival_city`**: The city where the flight arrives (e.g., "Mumbai").
8. **`flight_duration`**: The duration of the flight in minutes (e.g., `130` minutes).
9. **`stops`**: The number of stops made by the flight (e.g., `0` for non-stop flights).
10. **`price`**: The price of the flight (e.g., `5953`).
11. **`departure_time_group`**: The time group for departure (e.g., "Evening").
12. **`arrival_time_group`**: The time group for arrival (e.g., "Night").

#### Data Types of Columns:
- `flight_date`: datetime64[ns]
- `airline_name`: object
- `flight_code`: object
- `departure_time`: object
- `departure_city`: object
- `arrival_time`: object
- `arrival_city`: object
- `flight_duration`: int64
- `stops`: int64
- `price`: int64
- `departure_time_group`: object
- `arrival_time_group`: object

#### Missing Values per Column:
- No missing values in any of the columns.


## `clean_combined.csv`

This dataset combines the information from both business and economy class flights, including the flight details, departure and arrival times, duration, price, and more. It has been preprocessed and cleaned for further analysis.

#### DataFrame Shape:
- **Number of Rows**: 393,961
- **Number of Columns**: 12

#### Columns:
1. **`flight_date`**: The date on which the flight departs (e.g., "2022-02-11").
2. **`airline_name`**: The name of the airline operating the flight (e.g., "SpiceJet").
3. **`flight_code`**: The unique code assigned to each flight (e.g., "SG-8709").
4. **`departure_time`**: The time of departure (e.g., "18:55").
5. **`departure_city`**: The city from which the flight departs (e.g., "Delhi").
6. **`arrival_time`**: The time of arrival at the destination (e.g., "21:05").
7. **`arrival_city`**: The city where the flight arrives (e.g., "Mumbai").
8. **`flight_duration`**: The duration of the flight in minutes (e.g., `130` minutes).
9. **`stops`**: The number of stops made by the flight (e.g., `0` for non-stop flights).
10. **`price`**: The price of the flight (e.g., `5953`).
11. **`departure_time_group`**: The time group for departure (e.g., "Evening").
12. **`arrival_time_group`**: The time group for arrival (e.g., "Night").

#### Data Types of Columns:
- `flight_date`: datetime64[ns]
- `airline_name`: object
- `flight_code`: object
- `departure_time`: object
- `departure_city`: object
- `arrival_time`: object
- `arrival_city`: object
- `flight_duration`: int64
- `stops`: int64
- `price`: int64
- `departure_time_group`: object
- `arrival_time_group`: object

#### Missing Values per Column:
- No missing values in any of the columns.