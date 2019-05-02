# -*- coding: utf-8 -*-

"""
 @author      : Zhichuan Li   
 @mail        : lizhichuan2012@gmail.com
 @create date : 2019-04-23
 @Description : count number of each event_code
"""

import sqlite3
import pandas as pd
import numpy as np

stat_result = np.zeros(shape=(185, 2), dtype=int)

conn = sqlite3.connect('TSSC.db')   
c = conn.cursor()

# calculate number of event code from 1 to 185
for i in range(1, 186):
    print(i)
    c.execute('SELECT ifnull(Event_Code, 0) as code, count(Event_Code) as count FROM SIGNAL WHERE Event_Code=?', (i,))
    #print('count of event code: ', c.fetchall())
    df = pd.DataFrame(c.fetchall(), columns=['code','count'])
    event_code = df['code']
    event_count = df['count']
    stat_result[i-1][0] = event_code
    stat_result[i-1][1] = event_count

conn.close()

# show the result
#print(stat_result)    
dataset = pd.DataFrame({'code':stat_result[:,0],'count':stat_result[:,1]})
export_csv = dataset.to_csv('event_stat.csv', index=False)
# remove event code with 0 count
is_NoneZero = dataset['count'] > 0
dataset = dataset[is_NoneZero]
print(dataset)


plot = dataset.plot.bar(x='code', y='count', rot=40)
plot.set_xlabel("Event Code", fontname="Arial", fontsize=8)

# Change the y axis label to Arial
plot.set_ylabel("Count of event", fontname="Arial", fontsize=12)

# Set the title to Comic Sans
plot.set_title("Event code numbers ", fontname='Comic Sans MS', fontsize=18)

fig = plot.get_figure()
#fig.autofmt_xdate()
fig.savefig("event_stat.pdf")
print('result saved to pdf.')
