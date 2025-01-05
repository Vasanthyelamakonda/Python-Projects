ann_sal=float(input('Enter employee annual salary:'))
monthly_sal=ann_sal/12
if(monthly_sal>=50000):
    tax=12
    tax_amt=monthly_sal*tax/100
    final_sal=monthly_sal-tax_amt
    print('Tax :',tax,'%')
    print('Monthly Salary :',final_sal)
else:
    print('No Tax')
    print('Monthly salary :',monthly_sal)