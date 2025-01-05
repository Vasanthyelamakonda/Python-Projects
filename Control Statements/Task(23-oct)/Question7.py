n=int(input('Enter Starting Value :'))
m=int(input('Enter Ending Value :' ))
if(n>m):
    for i in range(n,m,-1):
        print( i, end='\t' )
else:
    for i in range(n,m):
        print(i , end='\t')
