import sqlite3
import csv

conn = sqlite3.connect('hurdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Year;
DROP TABLE IF EXISTS Mf;
DROP TABLE IF EXISTS Hurricanes;

CREATE TABLE Year (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    INTEGER UNIQUE
);

CREATE TABLE Mf (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Hurricanes (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    name TEXT  UNIQUE,
    year_id  INTEGER,
    mf_id INTEGER,
    dam INTEGER, death INTEGER
);
''')


fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'US_Atlantic_hurricanes.csv'
fh = open(fname)
file = fh.read()
data = file.splitlines()
count = 0
for line in data:
    count = count + 1
    if count == 1: continue
    # print(line)
    p = line.split(',')
    # print(p)
    hname = p[0].split('"')
    hname = hname[3]
    print(hname)
    yr = p[2]
    print(yr)
    dam = p[6]
    print(dam)
    # st = p[8]
    # print(st)
    dth = p[-3]
    print(dth)
    mf = p[-2].split('"')
    mf = mf[2]
    print(mf)

    cur.execute('''INSERT OR IGNORE INTO Year (title)
        VALUES ( ? )''', ( yr, ) )
    cur.execute('SELECT id FROM Year WHERE title = ? ', (yr, ))
    year_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Mf (name) 
        VALUES ( ? )''', ( mf, ) )
    cur.execute('SELECT id FROM Mf WHERE name = ? ', (mf, ))
    mf_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Hurricanes
        (name, year_id, mf_id, dam, death) 
        VALUES ( ?, ?, ?, ?, ? )''', 
        ( hname, year_id, mf_id, dam, dth, ) )

conn.commit()
cur.close()
