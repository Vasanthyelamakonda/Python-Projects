pcost=float(input('Enter Product Cost :'))
quantity=float(input('Enter Quantity :'))
cards=input('Enter Your Card name :')
bill=pcost*quantity
if(cards=='ICICI'):
    discount=15
    dis_amt=bill*discount/100
    final_amt=bill-dis_amt
    print('Bill Amount :',bill)
    print('Discount :',discount,'%')
    print('Discount Amount :',dis_amt)
    print('Final Bill Amount :',final_amt)
else:
    print('Final Bill Amount',bill)