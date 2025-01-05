import pyodbc as sql

con=sql.connect(driver='SQL Server',server='VASANTH\\SQLEXPRESS',database='project_menucard',username='sa',password='8889')
print('Connection Established')
cur=con.cursor()
ch='y'
while(ch=='y'):
    q='insert into productinfo values(?,?,?)'
    product_id=int(input('Enter Product ID :'))
    product_name=input('Enter Product Name :')
    cost=float(input('Enter Cost :'))
    t1=(product_id,product_name,cost)
    cur.execute(q,t1)
    con.commit()
    print('Data Inserted')
    ch=input('Do you want to continue(y/n) :')
con.close()
print('Connection Closed')
