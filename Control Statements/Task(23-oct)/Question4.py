n=int(input('Enter any Number :'))
print('Even Numbers are:', end='\t')
for i in range(1,n+1):
    if(i%2==0):
        print(i, end='\t')
