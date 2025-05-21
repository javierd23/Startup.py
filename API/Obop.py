#working with SQL lite. inserting data in SQLlite.
import sqlite3

conn = sqlite3.connect('rd.sqlite') #make sure you add the name of the file you need to creat on her
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

org_email = [] #this list cannot be used to add data to the sql so I made a for loop.
fname = input('Enter file name: ')
file = open(fname)
for lines in file:
    if lines.startswith('From '):   #from line 14 to 19 represent the codes to get the emial form the fiel/ next time i'll use reguex
        lines = lines.split()
        orgs = lines[1].split('@')
        org_email.append(orgs[1])
        for org in org_email:
            org = org.lower() #this is to get variable to the database

        cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

        conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
     print(str(row[0]), row[1])

cur.close()

