class google:
    def hr(self):
        self.a=2
        print(self.a)
class yahoo(google):
    super().hr()
    def developer(self):

        self.b=4
        print(self.b)
class mozilla(yahoo):
    super().developer()
    def __init__(self):

        c=self.a+self.b
        print(c)
c1=mozilla()
c1.hr()
c1.developer()
