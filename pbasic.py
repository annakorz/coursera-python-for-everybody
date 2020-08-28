import sqlite3
import time
import zlib

howmany = int(input("How many to dump? "))

conn = sqlite3.connect('hurdb.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, name FROM Hurricanes')
hurricanes = dict()
for message_row in cur :
    hurricanes[message_row[0]] = message_row[1]
#     print(hurricanes[message_row[0]])

# print(hurricanes)

cur.execute('SELECT id, title FROM Year')
years = dict()
for message_row in cur :
    years[message_row[0]] = message_row[1]
    # print(years[message_row[0]])

# print(years)

cur.execute('SELECT id, name, year_id, mf_id, dam, death FROM Hurricanes')
data = dict()
for message_row in cur :
    data[message_row[0]] = (message_row[0],message_row[1],message_row[2],message_row[4], message_row[5])
#     print(data[message_row[0]])

# print(data)

print("Loaded data=",len(data),"years=",len(years),"hurricanes=",len(hurricanes))

hurdam = dict()
hurdeath = dict()
for (data_id, data) in list(data.items()):
    hname = data[0]
    # hyear = data[2]
    # print(hname)
    damage = data[3]
    # print(damage)
    hurdam.update({hname : damage})
    death = data[4]
    # print(death)
    hurdeath.update({hname : death})
    
# print(hurdam) 
# print(hurdeath)

print('')
print('Top',howmany,'destructive hurricanes (in $ millions of damage)')

x = sorted(hurdam, key=hurdam.get, reverse=True)
for k in x[:howmany]:
    print(hurricanes[k], ': ', hurdam[k])
    if hurdam[k] < 10 : break

print('')
print('Top',howmany,'killing hurricanes (by number of people died)')

x = sorted(hurdeath, key=hurdeath.get, reverse=True)
for k in x[:howmany]:
    print(hurricanes[k], ': ', hurdeath[k])
    if hurdeath[k] < 10 : break
