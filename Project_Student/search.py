import pyodbc as sql
con = sql.connect(driver='SQL Server', server='VASANTH\\SQLEXPRESS', database='project_student', username='sa', password='8889')
print('Connection Established')
cur = con.cursor()
q = 'SELECT * FROM studentinfo WHERE sid=?'
sid = int(input('Enter Student ID: '))
t1 = (sid,)
cur.execute(q, t1)
data = cur.fetchall()
if len(data) == 0:
    print('Invaild Hall-Ticket Number')
else:
    for i in data:
        for j in i:
            print(j, end='\t')
        print()
con.close()
print('Connection Closed')
