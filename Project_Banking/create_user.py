import pyodbc as sql
con=sql.connect(driver='SQL Server',server='VASANTH\\SQLEXPRESS',database='project_banking',username='sa',password='8889')
print('Connection Established')
cur=con.cursor()
q = 'insert into customer values (?,?,?,?)'
def create_user():
    account_no=int(input('Enter Account Number :'))
    customer_name=input('Enter Customer Name :')
    gender=input('Gender :')
    amount=float(input('Enter Amount :'))
    return account_no, customer_name, gender, amount
user=create_user()
cur.execute(q,user)
con.commit()
con.close()
print('Connection Closed')
