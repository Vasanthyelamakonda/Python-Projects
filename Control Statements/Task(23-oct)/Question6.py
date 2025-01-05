n=int(input('Enter any number :'))
print('ODD', end='\t')
print('Even', end ='\n')
for i in range(1,n+1):
    if(i%2==0):
        print(i, end='\n')
    if(i%2!=0):
        print(i, end='\t')

