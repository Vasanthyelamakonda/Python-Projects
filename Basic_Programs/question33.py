Annual_salary=float(input("Enter annual salary:"))
hike=float(input("Enter hike percentage:"))
hike_salary=Annual_salary*hike/100
new_salary=Annual_salary+hike_salary
monthly_salary=new_salary/12
print("Updated Salary :", new_salary)
print("Updated Monthly Salary :",monthly_salary)
