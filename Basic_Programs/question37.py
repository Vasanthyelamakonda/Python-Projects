mango_cost=float(input("Enter the cost of Mango per KG :"))
quantity=float(input("Enter quantity :"))
discount=22
bill=mango_cost*quantity
discount_amt=bill*discount/100
final_amt=bill-discount_amt
print("Bill:",bill)
print("Discount Amount :",discount_amt)
print("Your total bill :",final_amt)