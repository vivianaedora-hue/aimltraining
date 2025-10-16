class Account:
    def _init_(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal

    def deposit(self, amount):
        self.bal+=amount
        print('Balance after deposit',self.bal)
    
    def withdraw(self,amount):
        if(self.bal>=amount):
            self.bal-=amount
            print('Balance after withdraw: ',self.bal)
        else:
            print('Insufficient amount in account')
            print('Transaction failed!!!')
    def show(self):
        print(f'Account holder name: {self.ac_holder} Account balance {self.bal}')

# ac1=Account('sameer',50000)
# ac2=Account('Chang',14000)
# ac1.show()
# ac2.show()
ac1=Account('sameer',50000)

ac1.show()
wamount=float(input('Enter amount to withdraw'))
ac1.withdraw(wamount)

class Account:
    def _init_(self, balance,ac_holder):
        self. _balance = balance
        self.ac_holder=ac_holder

    def get_balance(self):
        return self._balance
    


# acc = Account(1000,'Sam')
# acc.balance=34000
# print(acc.balance)


class Account:
    def _init_(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal
       
    def deposit(self, amount):
        self.bal+=amount
        print('Balance after deposit',self.bal)

    def withdraw(self,amount):
        if(self.bal>=amount):
            self.bal-=amount
            print('Balance after withdraw: ',self.bal)
        else:
            print('Insufficient amount in account')
            print('Transaction failed!!!')
    def show(self):
        print(f'Account holder name: {self.ac_holder} Account balance {self.bal}')

ac=Account('Sam',15000)
ac.show()
# ac1=Account('Raj',50000)
# # ac1.show()
print('Please choose\n 1.Deposit 2.Withdraw')
op=int(input())

if(op==1):
    damount=float(input('Enter amount to deposit'))
    ac.deposit(damount)
elif(op==2):
    damount=float(input('Enter amount to withdraw'))
    ac.withdraw(damount)   
#choice can be replaced with num -- it is variable
elif(op==3):
    ac.show()
else:
    print('Wrong choice')

