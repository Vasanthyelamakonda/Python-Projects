class rbi:
    def __init__(self):
        self.a=2
        print(self.a)
class sbi(rbi):
    def s_show(self):
        self.b=self.a+10
        print(self.b)
class credit_card:
    def c_show(self):
        c=self.a+self.b
        print(c)
        self.c=c
class atm(sbi,credit_card):
    def show(self):
        print(self.c)
c1=atm()
c2=credit_card()
c2.c_show()