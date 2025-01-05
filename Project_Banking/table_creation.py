import pyodbc as sql
con=sql.connect(driver='SQL Server',server='VASANTH\\SQLEXPRESS',database='project_banking',username='sa',password='8889')
print('Connection Established')
cur=con.cursor()
q='create table transfer(tr_id int identity (1101,1),account_no int references customer(account_no),tr_type char(5),amount money)'
cur.execute(q)
con.commit()
print('Tables created')
con.close()
print('Connection Closed')
