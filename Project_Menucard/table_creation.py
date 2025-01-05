import pyodbc as sql

con=sql.connect(driver='SQL Server',server='VASANTH\\SQLEXPRESS',database='project_menucard',username='sa',password='8889')
print('Connection Established')
cur=con.cursor()
q='create table productinfo(product_id int primary key,product_name varchar(20),cost money)'
cur.execute(q)
con.commit()
print('Table created')
con.close()
print('Connection Closed')
