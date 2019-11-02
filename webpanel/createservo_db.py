import sqlite3

conn = sqlite3.connect('servo_database.db')
print ("Opened database successfully");

conn.execute('CREATE TABLE servo (serv_id INTEGER, deg_min INTEGER, deg_max INTEGER, sleep_min INTEGER, sleep_max INTEGER ,extra TEXT)')
print ("Table created successfully");
conn.close()