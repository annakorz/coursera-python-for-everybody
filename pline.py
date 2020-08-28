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
    # print(hname)
    damage = data[3]
    # print(damage)
    hurdam.update({hname : damage})
    death = data[4]
    # print(death)
    hurdeath.update({hname : death})


# print("Top 10 Destructive Hurricanes")
# hurs = sorted(hurdam, key=hurdam.get, reverse=True)
# # print(hurs)
# count = 0
# for k in hurs:
#     x = str(hurricanes[k] + ': ') + str(hurdam[k])
#     print(x)
#     count = count + 1
#     if count > 10: break
#     # if hurdam[k] < 10 : break

# print('')
# print("Top 10 Deathly Hurricanes")
# hlist = sorted(hurdeath, key=hurdeath.get, reverse=True)
# count = 0
# for k in hlist:
#     y = str(hurricanes[k] + ': ') + str(hurdeath[k])
#     print(y)
#     count = count + 1
#     if count > 10: break
#     # if hurdam[k] < 10 : break

# cur.execute('SELECT h.name, h.death, y.title FROM Hurricanes AS h JOIN Year AS y ON h.year_id = y.Id')
# data = dict()
# for message_row in cur :
#     data[message_row[0]] = (message_row[1],message_row[2])

# hurdam = dict()
# hurdeath = dict()
# hur_year = dict()
# for d in list(data.items()):
#     print(d )
#     hname = d[0]
#     # print(hname)
#     # damage = data[3]
#     # print(damage)
#     # hurdam.update({hname : damage})
#     death = d[1]
#     print(death)
#     hurdeath.update({hname : death})
#     year = d[2]
#     print(year)
#     hur_year.update({hname: year})

# print(hurdeath)
# print(hur_year)

# sdata = sorted(data, key=lambda hur: hur[1])
# print('-----------------------------')
# print(sdata)

index = list()
hdeath = list()
# hyear = list()
hlist = sorted(hurdeath, key=hurdeath.get, reverse=True)
# print(hlist)
count = 0
for k in hlist:
    # print(k)
    index.append(hurricanes[k])
    hdeath.append(hurdeath[k])
    # hyear.append(data[k][1])
    count = count + 1
    if count == 10: break

# print(index)    
# print(hdeath)
# print(hyear)



# ylist = sorted(years, key=years.get, reverse=True)

# hdeath = [200, 416, 75, 256, 117, 62, 65, 1836, 84, 159]
# index = ['Diane', 'Audrey', 'Betsy', 'Camille', 'Agnes', 'Andrew', 'Rita', 'Katrina', 'Ike', 'Sandy']

df = pd.DataFrame({'Hurricanes' : index, 'Deaths' : hdeath})
ax = df.plot.bar(x='Hurricanes', y='Deaths',rot=0)
# df = pd.DataFrame({'hurricane' : hdeath}, index=index)
# ax = df.plot.bar(rot=0)
plt.show(block=True)

