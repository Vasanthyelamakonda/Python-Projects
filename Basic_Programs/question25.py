loan=500000
time=4
roi=11.4/100
intrest=loan*time*roi
final_amt=loan+intrest
monthly_intrest=roi/12
n=time*12
emi=loan*roi*(1+monthly_intrest)**n/(1+monthly_intrest)**n-1
print("EMI :",emi)
print("Intrest Amount:",intrest)
print("Total Amount:",final_amt)