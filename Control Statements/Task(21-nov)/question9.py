class sbi:
    def __init__(self):
        print('services from sbi')
class credit_card(sbi):
    def __init__(self):
        print('services from credit card')
class atm(credit_card):
    def __init__(self):
        print('services from atm')
c1=atm()
c2=credit_card()
c3=sbi()
