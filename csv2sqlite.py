# -*- coding: utf-8 -*-

"""
 @author      : Zhichuan Li   
 @mail        : lizhichuan2012@gmail.com
 @create date : 2019-04-22
 @Description : import csv file to sqlite database
 @Reference   : https://datatofish.com/create-database-python-using-sqlite3/
"""

import sqlite3
import pandas as pd
from pandas import DataFrame

db_name = 'TSSC.db'                  # database name
#db_name = 'test.db'                  # test code
conn = sqlite3.connect(db_name)      # You can create a new database
c = conn.cursor()                    # The database will be saved in the location where your file is saved

# Create table - signal
#c.execute('''DROP TABLE IF EXISTS SIGNAL''')
c.execute('''CREATE TABLE IF NOT EXISTS SIGNAL 
             ([Signal_ID] integer,
             [Datetime] date, 
             [Event_Code] integer, 
             [Event_Parameter] integer);''')

# create indexs
#c.execute('''CREATE INDEX index_signal ON SIGNAL (Signal_ID); ''')
#c.execute('''CREATE INDEX index_event ON SIGNAL (Event_Code); ''')

conn.commit()

file_folder = "D:\\03_Projects\\git_repository\\datasets\\TSSC2019"
#signalid_list = [7076,7122,7123,7124,7125,7126,7127,7128,7129,7180,7181,7182,7183,7184,7185,7186,7187,7188,7189,7190,7241,7342]
#signalid_list = [7076,7122,7123,7124,7125,7126,7127,7128,7129,7180,7181,7182]   # test code
signalid_list = [7183,7184,7185,7186,7187,7188,7189,7190,7241,7342]
#signalid_list = [7076]

for signalid in signalid_list:
    for month in range(1,13):
        file_name = str(month) +"_" + str(signalid) + ".csv"        # 1_7076.csv ...12_7076.csv
        file_path = file_folder +"\\"+ str(signalid) + "\\"+ str(file_name)
        print(file_path)
        df = pd.read_csv (file_path)
        df.columns = ['Signal_ID','Datetime','Event_Code','Event_Parameter']
        df.to_sql('SIGNAL', conn, if_exists='append', index = False) 
        # Insert the values from the csv file into the table 'CLIENTS' 

# select first 5 rows from table
c.execute('SELECT * FROM SIGNAL limit 5 ;')
#print(c.fetchall())
df = DataFrame(c.fetchall(), columns=['Signal_ID','Datetime','Event_Code','Event_Parameter'])
print(df)

conn.close()