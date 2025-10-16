class Emp:
    def _init_(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=qual

    def display(self):
        print('ID: ',self.id)
        print('Name: ',self.name)
        print('Quali: ',self.qual)

class Dev(Emp):
    def _init_(self, id, name, qual,domain,project):
        super()._init_(id, name, qual)
        self.domain=domain
        self.project=project

    def display(self):
        super().display()
        print('Domain: ',self.domain)
        print('Project: ',self.project)

#create one emp project with id=1, name='Sam', qual='MCA'
emp=Emp(1,'Sam','MCA')
#create one Dev object with id=3, name='Ravi', qual='MTech',Project='eShopping', Domain='dot net'
dev=Dev(3,'Ravi','MTech','e-shopping','dotnet')
#Display Dev details
print('Developer details as follows')
dev.display
#Display Emp details
print('Employee details as follows')
emp.display()
