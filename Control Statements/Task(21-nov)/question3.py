class google:
    def hr(self):
        self.a=2
        print(self.a)
class yahoo(google):
    def developer(self):
        super().hr()
        self.b=4
        print(self.b)
class mozilla(yahoo):
    def __init__(self):
        super().developer()
        c=self.a+self.b
        print(c)
c1=mozilla()
c1.hr()
c1.developer()
