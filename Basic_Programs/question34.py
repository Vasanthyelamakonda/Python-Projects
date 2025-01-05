value=float(input("Enter Market Value:"))
old_stamp_duty=5
new_stamp_duty=7
previous_duty_amount=(value*old_stamp_duty)/100
previous_amt=value+previous_duty_amount
new_duty_amount=(value*new_stamp_duty)/100
new_amt=value+new_duty_amount
diff_amt=new_amt-previous_amt
print("Previous duty amount :",previous_duty_amount)
print("Previous payable amount with 5% stamp duty:",previous_amt)
print("New duty amount:",new_duty_amount)
print("New payable amount with 7% stamp duty:",new_amt)
print("Differnce between previous and new payable amount :", diff_amt)
