class google:
    def show(self):
        print('google')
class yahoo(google):
    def display(self):
        print('yahoo')
class mozilla(yahoo,google):
    def register(self):
        print('mozilla')
c1=mozilla()
c1.show()
c1.display()
c1.register()