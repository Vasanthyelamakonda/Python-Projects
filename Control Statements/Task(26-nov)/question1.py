import sqlite3 as sql

con=sql.connect('Amazon')
print('Connection Established')
cur=con.cursor()
cur.execute('insert into product values(1101,"Bourboun",40.0,100,"2025-06-06")')
con.commit()
print('Data Inserted')
con.close()
print('Connection Closed')