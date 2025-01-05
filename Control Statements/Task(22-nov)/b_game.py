import random
points=0
ch='y'
while(ch=='y'):
    a=random.randint(1,15)
    b=random.randint(1,15)
    print('First Number :',a)
    print('Second Number :',b)
    c=int(input('Enter Product of a,b :'))
    d=a*b
    if(d==c):
        points+=5
    ch = input('Enter your choice(y/n):')
if(points>=50):
    print('Aahh Aatagadivey')
    print('Laksha Rupees Vachinau Ra Neku')
elif(points>=30 and points<=49):
    print('Inka Baga chadhavali sare na')
elif(points>=20 and points<=29):
    print('Bag reday cheysuko ega school ki time aiythundhi')
else:
    print('Ra ra first nuvu School ki yellu ')
print('Neku Vachina points :',points)