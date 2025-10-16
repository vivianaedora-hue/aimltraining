# class Emp:
#     def display(self):
#         print('Display of employee class')


# obj = Emp()
# obj.display()

# #class className:
#     #definition of class
#     #attribute method, constructors

# #objectName=ClassName()
# # objectName.MethodName()

# e=Emp()
# e.display()

#second example
class Emp:
    def reg(self,eid,ename):
        self.eid=eid
        self.ename=ename
        
    def display(self):
        print('Employee details as folows')
        print('Employee id:',self.eid)
        print('Émployee name:',self.ename)
              
e1 = Emp()
e2 = Emp()
e3 = Emp()
e1.reg(1,'Sam')
e2.reg(102,'Neha')
e3.reg(103,'Jai')
print('First employee details')
e1.display()
print('Second employee details')
e2.display()
print('Third employee details')
e3.display()
