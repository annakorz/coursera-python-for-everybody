import sqlite3
import time
import zlib
import string
import random

conn = sqlite3.connect('hurdb.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, name FROM Hurricanes')
hurricanes = dict()
for message_row in cur :
    hurricanes[message_row[0]] = message_row[1]
    # print(hurricanes[message_row[0]])

print(hurricanes)

cur.execute('SELECT id, name, year_id, mf_id, dam, death FROM Hurricanes')
data = dict()
for message_row in cur :
    data[message_row[0]] = (message_row[0],message_row[1],message_row[2],message_row[4], message_row[5])

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

# x = sorted(hurdam, key=hurdam.get, reverse=True)
# for k in x:
#     print(hurricanes[k], ': ', hurdam[k])
#     if hurdam[k] < 10 : break

x = sorted(hurricanes, key=hurricanes.get, reverse=True)
highest = None
lowest = None
for k in x:
    if highest is None or highest < hurricanes[k] :
        highest = hurricanes[k]
    if lowest is None or lowest > hurricanes[k] :
        lowest = hurricanes[k]
print('Range of counts:',highest,lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('gword.js','w')
fhand.write("gword = [")
first = True
for k in x[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = hurricanes[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

print("Output written to gword.js")
print("Open gword.htm in a browser to see the vizualization")
