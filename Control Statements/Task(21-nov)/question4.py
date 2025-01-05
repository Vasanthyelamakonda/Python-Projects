class google:
    def hr(self):
        a=2
        print(a)
class yahoo(google):
    def developer(self):
        super().hr()
        b=4
        print(b)
class mozilla(yahoo):
    def __init__(self):
        super().developer()
        c=a+b
        print(c)
c1=mozilla()
c1.hr()
c1.developer()
