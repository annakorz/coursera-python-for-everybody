import sqlite3
import time
import zlib
import matplotlib.pyplot as plt
import pandas as pd

conn = sqlite3.connect('hurdb.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, name FROM Hurricanes')
hurricanes = dict()
for message_row in cur :
    hurricanes[message_row[0]] = message_row[1]

cur.execute('SELECT id, title FROM Year')
years = dict()
for message_row in cur :
    years[message_row[0]] = message_row[1]


cur.execute('SELECT id, name, year_id, mf_id, dam, death FROM Hurricanes')
data = dict()
for message_row in cur :
    data[message_row[0]] = (message_row[0],message_row[1],message_row[2],message_row[4], message_row[5])

print("Loaded data=",len(data),"years=",len(years),"hurricanes=",len(hurricanes))

hurdam = dict()
hurdeath = dict()
for (data_id, data) in list(data.items()):
    hname = data[0]
    damage = data[3]
    hurdam.update({hname : damage})
    death = data[4]
    hurdeath.update({hname : death})

index = list()
hdeath = list()
hlist = sorted(hurdeath, key=hurdeath.get, reverse=True)
count = 0
for k in hlist:
    index.append(hurricanes[k])
    hdeath.append(hurdeath[k])
    count = count + 1
    if count == 10: break

df = pd.DataFrame({'Hurricanes' : index, 'Deaths' : hdeath})
ax = df.plot.bar(x='Hurricanes', y='Deaths',rot=0)

plt.show(block=True)

