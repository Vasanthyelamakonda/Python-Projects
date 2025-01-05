import pyodbc as sql
con=sql.connect(driver='SQL Server',server='VASANTH\\SQLEXPRESS',database='project_student',username='sa',password='8889')
print('Connection Established')
cur=con.cursor()
q='insert into studentinfo values(?,?,?,?,?,?,?,?,?,?)'
sid=int(input('Enter Student ID :'))
sname=input('Enter Student Name :')
gender=input('Enter Gender :')
s1=int(input('Enter Subject-1 Marks :'))
s2=int(input('Enter Subject-2 Marks :'))
s3=int(input('Enter Subject-3 Marks :'))
total=s1+s2+s3
average=total/3
grade=''
result=''
if(s1>35 and s2>35 and s3>35):
    result='Pass'
    if(average>90):
        grade='O'
    elif(average>80 and average<=90):
        grade='A+'
    elif(average>70 and average<=80):
        grade='A'
    elif(average>60 and average<=70):
        grade='B+'
    elif(average>50 and average<=60):
        grade='B'
    else:
        grade='c'
else:
    grade='D'
    result = 'Fail'
t1=(sid,sname,gender,s1,s2,s3,total,average,grade,result)
cur.execute(q,t1)
con.commit()
print('Data Inserted')
con.close()
print('Connection Closed')