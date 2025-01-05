cost=float(input('Enter Ticket Cost :'))
tickets=int(input('Enter No. of Tickets :'))
coupon=input('Enter Coupon Code :')
bill=cost*tickets
if(coupon=='SAVE20'):
    discount=20
    dis_amt=bill*20/100
    final_amt=bill-dis_amt
    print('Bill :',bill)
    print('Discount :',discount)
    print('Discount Amount',dis_amt)
    print('Final Bill :',final_amt)
else:
    print("Final Bill :",bill)