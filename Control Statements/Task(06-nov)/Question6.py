a=[5,9,12,15,4]
s=a[0]
b=a[0]
for i in a:
    if(i<s):
        s=i
print('smallest number is :',s)
for i in a:
    if(i>b):
        b=i
print('Biggest number is :',b)
diff=b-s
print('Difference is :',diff)


