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

### `clean_dataset_df.csv` Description

This dataset contains flight information related to different airlines. Each row represents a flight and includes various details about the flight and its pricing.

#### Columns:

1. **`airline_name`**: The name of the airline operating the flight (e.g., "SpiceJet", "Air Asia", "Vistara").
2. **`flight_code`**: The unique code assigned to each flight (e.g., "SG-8709", "I5-764", "UK-995").
3. **`departure_city`**: The city from which the flight departs (e.g., "Delhi").
4. **`arrival_city`**: The destination city where the flight lands (e.g., "Mumbai").
5. **`flight_duration`**: The duration of the flight in minutes (e.g., `130` minutes).
6. **`stops`**: The number of stops the flight makes on its route (e.g., `0` for non-stop flights).
7. **`price`**: The price of the flight in Indian Rupees (INR) (e.g., `5953`).
8. **`class`**: The class of the seat, such as "Economy".
9. **`days_left`**: The number of days remaining until the flight departs (e.g., `1` day).
10. **`departure_time_group`**: The time group in which the flight departs, categorized into various time slots (e.g., "Evening", "Morning").
11. **`arrival_time_group`**: The time group in which the flight arrives at its destination (e.g., "Night", "Afternoon").


### `clean_business_df.csv` Description

This dataset contains detailed information about business class flights, including the flight date, airline, schedule, duration, price, and other relevant details. Each row represents a business class flight.

#### Columns:

1. **`flight_date`**: The date of the flight (e.g., "2022-02-11").
2. **`airline_name`**: The name of the airline operating the flight (e.g., "Air India").
3. **`flight_code`**: The unique code assigned to each flight (e.g., "AI-868", "AI-531").
4. **`departure_time`**: The time when the flight departs (e.g., "18:00").
5. **`departure_city`**: The city from which the flight departs (e.g., "Delhi").
6. **`arrival_time`**: The time when the flight arrives at its destination (e.g., "20:00").
7. **`arrival_city`**: The city where the flight arrives (e.g., "Mumbai").
8. **`flight_duration`**: The duration of the flight in minutes (e.g., `120` minutes).
9. **`stops`**: The number of stops made by the flight (e.g., `0` for non-stop flights).
10. **`price`**: The price of the flight in Indian Rupees (INR) (e.g., `25612`).
11. **`departure_time_group`**: The time group in which the flight departs, categorized into various time slots (e.g., "Evening", "Afternoon").
12. **`arrival_time_group`**: The time group in which the flight arrives at its destination (e.g., "Evening", "Night").


### `clean_economy_df.csv` Description

This dataset contains detailed information about economy class flights, including the flight date, airline, schedule, duration, price, and other relevant details. Each row represents an economy class flight.

#### Columns:

1. **`flight_date`**: The date of the flight (e.g., "2022-02-11").
2. **`airline_name`**: The name of the airline operating the flight (e.g., "SpiceJet").
3. **`flight_code`**: The unique code assigned to each flight (e.g., "SG-8709", "I5-764").
4. **`departure_time`**: The time when the flight departs (e.g., "18:55").
5. **`departure_city`**: The city from which the flight departs (e.g., "Delhi").
6. **`arrival_time`**: The time when the flight arrives at its destination (e.g., "21:05").
7. **`arrival_city`**: The city where the flight arrives (e.g., "Mumbai").
8. **`flight_duration`**: The duration of the flight in minutes (e.g., `130` minutes).
9. **`stops`**: The number of stops made by the flight (e.g., `0` for non-stop flights).
10. **`price`**: The price of the flight in Indian Rupees (INR) (e.g., `5953`).
11. **`departure_time_group`**: The time group in which the flight departs, categorized into various time slots (e.g., "Evening", "Morning").
12. **`arrival_time_group`**: The time group in which the flight arrives at its destination (e.g., "Night", "Morning").
