class Player:
    def _init_(self):
        print('Welcome to player class')

    def reg(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team

    def display(self):
        print(f'Id: {self.id} \t Name: {self.name} \t Team: {self.team} ')

#object creation
p1=Player()
p2=Player()
p3=Player()
p1.reg(1,'MSD','India')
p2.reg(2,'R.Khan','Afghanistan')
p2.reg(3,'Moin Ali','England')

p1.display()
p2.display()
p3.display()


#parameterize constructor
class Player:
    def _init_(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team

    def display(self):
        print(f'Id: {self.id} \t Name: {self.name} \t Team: {self.team} ')
       
    def __str__(self):
         return f'{self.id} {self.name} {self.team} '


#object creation

p1.reg(1,'MSD','India')
p2.reg(2,'Moin Ali','England')
p2.reg(3,'Joe Root','England')

#display first player details
p1.display()
p2.display()
p3.display()

print(p1)
print(p2)
print(p3)
