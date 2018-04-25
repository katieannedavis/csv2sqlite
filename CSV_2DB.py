# This program will take the data in a csv (comma separated values) file and put it in an sqlite database

#!/usr/bin/python
import csv, sqlite3

# Open csv document and reader it
f = open('Databases\MOCK_DATA.csv', 'r')
next(f, None)
reader = csv.reader(f)

# Establish connection to database
connection = sqlite3.connect('Databases\BusinessContacts.db')
pointer = connection.cursor()

# Create table and columns
pointer.execute('''CREATE TABLE IF NOT EXISTS contacts (
    id int, 
    name varchar(255), 
    street varchar(255), 
    city varchar(255),
    state varchar(255),
    country varchar(255),
    contact varchar(255),
    email varchar(255),
    department varchar(255)
);''')
# Populate rows
data = []
for row in reader:
    data += [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])]
pointer.executemany('INSERT INTO contacts VALUES(?,?,?,?,?,?,?,?,?)', data)
# Save data
connection.commit()
# Close connection to database
connection.close()
