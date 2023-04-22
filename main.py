from dentist_scrape_engine import get_data_api , insert_data_db, write_data_csv

city_scrape = 'New York'

if __name__ == '__main__':
    data = get_data_api(city_scrape)
    insert_data_db(data)
    write_data_csv(data)


