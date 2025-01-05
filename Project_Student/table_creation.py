import pyodbc as sql
con=sql.connect(driver='SQL Server',server='VASANTH\\SQLEXPRESS',database='project_student',username='sa',password='8889')
print('Connection Established')
cur=con.cursor()
q='create table studentinfo(sid int primary key,sname varchar(20),gender char(2),s1 int , s2 int, s3 int,total int,average float,grade char(3),result char(10))'
cur.execute(q)
con.commit()
print('Table created')
con.close()
print('Connection Closed')