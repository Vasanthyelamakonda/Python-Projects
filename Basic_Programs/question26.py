last_reading=2234
current_reading=2456
units_consumed=current_reading-last_reading
service_charge=30
month_days=30
per_unit_cost=3.46
tax=0.06
bill=units_consumed*per_unit_cost*tax*month_days+service_charge
print("Total Bill is :",bill)
