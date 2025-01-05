class sbi:
    def show(self):
        print('services from sbi')
class credit_card(sbi):
    def show(self):
        print('services from credit card')
class atm(credit_card):
    def show(self):
        print('services from atm')
c1=atm()
c1.show()