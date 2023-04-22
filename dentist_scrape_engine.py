import requests
import sqlite3
import logging
import csv
import urllib.parse
import json

logging.basicConfig(level=logging.ERROR, filename="scraper.log", format='%(asctime)s,%(levelname)s, %(message)s')


#Get the data from the API
def get_data_api(target_city):
        city = urllib.parse.quote(target_city)
        
        url = f"https://www.deltadental.com/conf/ddpa/paths/dentistsearchrest.json?maximumDistance=100&sortType=0&productCode=PPO&maximumNumberOfRecordsToReturn=250&city={city}"

        headers = {                     
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-language': 'en,en-US;q=0.9,ro;q=0.8',       
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
                }

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                print('Success Request!')
                
                json_respose = response.json()
            return json_respose['listOfLocations']
        
        except Exception:
            print('Failed, Check the logs file!')

            logging.exception('Error Found!')
            return None


#Insert data into sqlite3 database       
def insert_data_db(json_data):
        
        print('Data uploading to DB..')
        
        data_list = []    

        for x in json_data:

            dict_data = {
                        'firstname': x['firstName'],
                        'lastname': x['lastName'],
                        'businessName': x['businessName'],
                        'address': x['addressOne'],
                        'state': x['stateCode'],
                        'zip': x['zip'],
                        'phone': x['telephoneNumber'],
                        'email': x.get('officeEmail')
                        }
            
            data_list.append(dict_data)            

        with sqlite3.connect('dental_data.db') as connection:

            c = connection.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS dental_info(firstname text, lastname text, business_name text,address text,state text,zip text,phone text,email text)')
            
            for data in data_list:
                c.execute('INSERT INTO dental_info VALUES(:firstname,:lastname,:businessName,:address,:state,:zip,:phone,:email)',data)

#Insert data into CSV
def write_data_csv(json_data,newline=''):

    with open('dental_data.csv', 'w') as csv_file:

        fieldnames = ['firstname', 'lastname', 'businessName', 'address', 'state', 'zip', 'phone', 'email']       
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()

        for x in json_data:
             
            dict_data = {
                    'firstname': x['firstName'],
                    'lastname': x['lastName'],
                    'businessName': x['businessName'],
                    'address': x['addressOne'],
                    'state': x['stateCode'],
                    'zip': x['zip'],
                    'phone': x['telephoneNumber'],
                    'email': x.get('officeEmail')
                    }
            
            writer.writerow(dict_data)

    print('Data has been writen in csv file!')
