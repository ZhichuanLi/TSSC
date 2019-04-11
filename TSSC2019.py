# -*- coding: utf-8 -*-

"""
 @author      : Zhichuan Li   
 @mail        : lizhichuan2012@gmail.com
 @create date : 2019-04-10
 @Description : Source code for TSSC2019 big data challange
"""

import csv

# load dataset

# total 22 signal ID
# each signal ID contains 12 csv files which represent the 12 months' data. naming:<month-number>_<signalid>
home_folder = "D:\\03_Projects\\git_repository\\dataset\\TSSC2019"
signalid_list = [7076,7122,7123,7124,7125,7126,7127,7128,7129,7180,7181,7182,7183,7184,7185,7186,7187,7188,7189,7190,7241,7342]
#signalid_list = [7076,7122]
file_count = 0            # umber of files
eventcode_exception = 0   # number of records that contains undefined event code
row_count = 0           # total number of records in all files

for signalid in signalid_list:
    for month in range(1,13):
        file_name = str(month) +"_" + str(signalid) + ".csv"        # 1_7076.csv ...12_7076.csv
        file_path = home_folder +"\\"+ str(signalid) + "\\"+ str(file_name)
        print(file_path)
        with open(file_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            # row format: "signalid","datetime","event code","event parameter"
            for row in readCSV:
                row_count += 1
                # calculate how many event code greater than 185
                event_code = row[2]
                if int(event_code) > 185:
                    eventcode_exception += 1
        file_count += 1

print("total " + str(file_count) + " files from dataset.")
print("total " + str(row_count) + " records.")
print("total " + str(eventcode_exception) + " records contains undefined event code")
print("ratio: " + format(eventcode_exception/row_count,'.0%'))
        