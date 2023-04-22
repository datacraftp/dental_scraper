# dental_scraper
Sure, here's some documentation for the code you provided:

Overview
This Python script is a web scraper that fetches data from an API and then saves the data to a SQLite database and a CSV file. The script takes a city name as input, fetches dental office data for that city from the Delta Dental API, and saves the data to a SQLite database and a CSV file.

The script uses the following modules:

sqlite3 for working with a SQLite database.
logging for logging error messages to a file.
csv for working with CSV files.
urllib.parse for URL encoding.
json for working with JSON data.
requests for sending HTTP requests to the Delta Dental API.
Required Modules

The following modules need to be installed in your Python environment in order to run this script:

sqlite3
logging
csv
urllib
json
requests
You can install the modules using the following command:

Copy code
pip install sqlite3 logging csv urllib3 json requests
How to use
Download the script to your computer.
Open the config.json file and change the target_city value to the name of the city you want to get data for.
Run the script using the command: python scraper.py
The script will fetch the data from the Delta Dental API, save it to a SQLite database and a CSV file, and print a message confirming that the data has been saved.

Functions
The script has three functions:

get_data_api(target_city)
This function takes a city name as input, fetches dental office data for that city from the Delta Dental API, and returns a list of dictionaries containing the data.

insert_data_db(json_data)
This function takes a list of dictionaries containing dental office data as input, and saves the data to a SQLite database.

write_data_csv(json_data)
This function takes a list of dictionaries containing dental office data as input, and saves the data to a CSV file.

