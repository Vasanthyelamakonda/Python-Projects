import pyodbc as sql

con=sql.connect(driver='SQL Server',server='VASANTH\\SQLEXPRESS',database='project_student',username='sa',password='8889')
print('Connection Established')
print(con)
con.close()
print('Connection Closed')
