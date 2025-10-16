class Bird:
    def fly(self):
        print('Bird can fly')

class Airplane(Bird):
    def fly(self):
        print('Airplane fly')

b=Bird()
print('Bird implement')
b.fly()

print('Airplane implementation')
a=Airplane()
a.fly()

print('Using for loop')
for obj in [Bird(), Airplane()]:
    obj.fly()
class Emp:
    def reg(self,id, name):
        self.id=int(input ('Enter Id:'))
        self.name=int(input ('Enter name:'))

        def disp(self):
            print('Name: ',self.name)
            print('Id: ',self.id)

class Dev:
    def reg(self):
        super().reg()
        self.domain=('Enter domain')

    def disp(self):
        super()
        print('Domain: ',self.domain)


d1=Dev()
d1.reg()
d1.disp()
