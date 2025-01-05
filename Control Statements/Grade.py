s1=int(input('Enter Sub-1 marks:'))
s2=int(input('Enter sub-2 marks:'))
s3=int(input('Enter sub-3 marks:'))
total=s1+s2+s3
avg=total/3
print('Total Marks:',total)
print('Average:',avg)
if(avg>=70):
    print('Grade-A')
elif(avg>=60 and avg<70):
    print('Grade-B')
elif(avg>=50 and avg<60):
    print('Grade-C')
else:
    print('Grade-D')

