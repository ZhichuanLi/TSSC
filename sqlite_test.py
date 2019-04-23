# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:38:31 2019

@author: lizhichuan
"""

import sqlite3
import pandas as pd
from pandas import DataFrame

con = sqlite3.connect('TestDB.db')

c = con.cursor()
#c.execute("DROP TABLE A;")

c.execute('SELECT * FROM SIGNAL_2 order by Datetime asc limit 5 ;')

#print(c.fetchall())

df = DataFrame(c.fetchall(), columns=['Signal_ID','Datetime','Event_Code','Event_Parameter'])
print (df) 
print(df['Event_Code'])