general_cost=460
hike=50
cost=general_cost*hike/100
new_cost=general_cost+cost
tickets=int(input("Enter No. of Tickets:"))
total=tickets*new_cost
print("Total Amount:",total)