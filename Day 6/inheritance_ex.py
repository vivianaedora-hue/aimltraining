#super class or base class or parent class
class Emp:
    def reg(self, id, name):
        self.id=id
        self.name=name
  
    def display(self, id, name):
        print('Id: ',self.id)
        print('Name: ',self.name)

#inherited class or derived class or child class
class Dev(Emp):
    def welcome(self):
        print('Welcome to developer')



d=Dev()
d.welcome()
d.reg(1,'Sam')
d.display()


e=Emp()
e.reg(102,'Raj')
e.display()