import pyodbc as sql
con=sql.connect(driver='SQL Server',server='VASANTH\\SQLEXPRESS',database='project_banking',username='sa',password='8889')
print('Connection Established')
cur=con.cursor()
print('1. Deposit')
print('2. Withdrawal')
print('3. Balance Enquiry')
print('4. Mini-Statement')
a=int(input('Select Your Options (1,2,3,4):'))
q = 'insert into transfer values (?,?,?)'
if(a==1):
    def deposit():
        account_no=int(input('Enter Account Number :'))
        tr_type='D'
        amount = float(input('Enter Amount :'))
        q1 = 'update customer set amount=amount+? where account_no=?'
        cur.execute(q1,(amount,account_no))
        con.commit()
        return account_no,tr_type,amount
    depo=deposit()
    cur.execute(q,depo)
    con.commit()
elif(a==2):
    def withdrawal():
        account_no = int(input('Enter Account Number :'))
        tr_type ='W'
        amount = float(input('Enter Amount :'))
        q2 = 'update customer set amount=amount-? where account_no=?'
        cur.execute(q2, (amount, account_no))
        con.commit()
        return account_no, tr_type, amount
    withdraw=withdrawal()
    cur.execute(q,withdraw)
    con.commit()
elif a == 3:
    def BalanceEnquiry():
        account_no = int(input('Enter Account Number: '))
        q3 = 'select account_no, amount, customer_name from customer where account_no = ?'
        cur.execute(q3, (account_no,))
        data = cur.fetchone()
        if (len(data)>0):
            print('Balance Enquiry')
            print(f'Account Number: {data[0]}')
            print(f'Customer Name: {data[2]}')
            print(f'Balance: {data[1]}')
        else:
            print('No Account Found')
    BalanceEnquiry()
elif(a==4):
    def Mini_Statement():
        account_no = int(input('Enter Account Number: '))
        q4 = 'select *from transfer where account_no = ?'
        cur.execute(q4, (account_no,))
        data2 = cur.fetchall()
        if (len(data2)>0):
            print('Mini-Statement')
            for i in data2:
                print('-----------------------------')
                print(f'Account Number   : {i[2]}')
                print(f'Transaction ID   : {i[0]}')
                print(f'Transaction Type : {i[1]}')
                print(f'Amount           : {i[3]}')
                print('-----------------------------')
        else:
            print('No Transactions Found')
    Mini_Statement()
else:
    print('!----Invalid Input----!')
con.close()
print('Connection Closed')
