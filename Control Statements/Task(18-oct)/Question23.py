age=int(input('Enter Your Age:'))
if(age<5):
    print('No Ticket')
elif(age>=5 and age<=12 or age>=60):
    print('Half Ticket')
else:
    print('Full Ticket')
