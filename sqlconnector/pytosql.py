import csv
import MySQLdb as db

mydb = db.connect(host = '127.0.0.1', user = 'root', password = 'Folashade@12', database = 'practice')

with open ('/Users/Dell/Downloads/Train_details.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter = ',')
    all_value = []
    for row in csvfile:
        value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        all_value.append(value)

query = "INSERT INTO all_db (train_no, station_code, station_name, arrival_time, departure_time, distance, source_station, source_station_name, destination_station, destination_station_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
mycursor = mydb.cursor()
mycursor.executemany(query, all_value)
mydb.commit()