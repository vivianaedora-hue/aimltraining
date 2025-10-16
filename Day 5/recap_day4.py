def display():
    print('Welcome to recap of functions')

def welcome(name):
    print('Welcome to functions Mr.\\Ms.',name)

def cube(num):
    cube_num=num*num*num
    print('Cube of given number: {num} is =\t {cube_num}')

def square(num):
    return num*num



def salBonus(salary):
    return num*num

# welcome('Vivi') 
# display()
# my_num=int(input('Enter number to find out cube:\t'))
# cube(my_num)
# username=input('Enter user name: \t')
# my_num=int(input('Enter number to find out cube and square: \t'))
# welcome(username)
# cube(my_num)
# square(my_num)


# sq=square(my_num)
# print(f'Square of {my_num} is: {sq}')
# print(f'Number: {my_num} Square: {sq}')
# my_sal=float(input('Enter salary to find out bonus: \t'))
# bonus=salBonus(my_sal)
# print(f'Salary {my_sal} Bonus: {bonus}')
# print(f'Salary after bonus =\t',(my_sal+bonus))

def salBonus(salary):
    bonus=salary*0.10
    print(f'Salary {salary} Bonus: {bonus}')

my_sal=float(input('Enter Salary to find out bonus: \t'))
salBonus(my_sal)
#print(f'Salary after bonus =\t',(my_sal+bonus))

