s1=int(input('Enter Sub-1 marks:'))
s2=int(input('Enter sub-2 marks:'))
s3=int(input('Enter sub-3 marks:'))
if(s1>=35 and s2>=35 and s3>=35):
    print('PASS')
    total=s1+s2+s3
    avg=total/3
    print('Total Marks:',total)
    print('Average:',avg)
else:
    print('Better Luck Next Time')
