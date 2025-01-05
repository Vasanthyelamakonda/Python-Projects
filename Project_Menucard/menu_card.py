from typing import final

import pyodbc as sql
from unicodedata import decimal

con=sql.connect(driver='SQL Server',server='VASANTH\\SQLEXPRESS',database='project_menucard',username='sa',password='8889')
print('Connection Established')
cur=con.cursor()
ch='y'
bill=0
while(ch=='y'):
    q='select * from productinfo'
    cur.execute(q)
    data=cur.fetchall()
    for i in data:
        for j in i:
            print(j,end='\t')
        print()
    q1='select cost from productinfo where product_id=?'
    product_id=int(input('Enter Item ID :'))
    t1=(product_id,)
    cur.execute(q1,t1)
    data1=cur.fetchall()
    if(len(data1)>0):
        for i in data1:
            for j in i:
                print('Cost is :',j)
        a=int(input('Enter Quantity :'))
        bill=bill+(a*j)
    else:
        print('Invalid Choice')
    ch=input('Do You want to Continue(y/n) :')
print('Bill Amount is :', bill)
if (bill > 300):
    discount = 20
else:
    discount = 0
print('Discount :', discount, '%')
discount_value = (bill * discount) / 100
print('Discount Amount :', discount_value)
cgst = 2.5
sgst = 2.5
total_tax = cgst + sgst
final_bill = float(bill - discount_value) + (float(bill) * total_tax / 100)
print('Final Bill :', final_bill)
c = int(input('Paid Amount :'))
print('Balance Amount :', final_bill - c)
con.close()
print('Connection Closed')
