import sqlite3 as sql

con=sql.connect('Mediplus')
print('Connection Established')
cur=con.cursor()
q='select * from Medical where MedName=?'
MedName=input('Enter Medicine Name :')
t1=(MedName,)
cur.execute(q,t1)
data=cur.fetchall()
for i in data:
    for j in i:
        print()

if( MedName in j):
    print('Medicine is Available')
else:
    print('Medicine is Not Available')
con.close()
print('Connection Closed')