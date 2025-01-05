cost=float(input('Enter cost:'))
quantity=float(input('Enter Quantity:'))
bill=cost*quantity
if(bill>5000):
    discount=20
    dis=bill*discount/100
    final_amt=bill-dis
    print('Bill Amount :',bill)
    print('Discount :',discount,'%')
    print('Discount Amount :',dis)
    print('Final Bill :',final_amt)
else:
    print('Bill Amount :',bill)

