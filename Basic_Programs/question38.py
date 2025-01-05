indian_airlines_price=3450
gst_indian_airlines=18
indigo_price=3200
gst_indigo=12
flight1_charges=(indian_airlines_price*18)/100
final_cost1=indian_airlines_price+flight1_charges
flight2_charges=(indigo_price*12)/100
final_cost2=indigo_price+flight2_charges
amount_saved=final_cost1-final_cost2
print("Ticket price for Indain Airlines :", final_cost1)
print("Ticket price for Indigo Airlines :", final_cost2)
print("Amount saved my Mr.Venkat Reddy :",amount_saved)