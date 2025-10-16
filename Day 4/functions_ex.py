
# def function_name(parameters):
#     '''docstring'''
#     statement(s)

#function without parameters
# def welcome():
#     print("Welcome to Functions")
#     print("Our first Function ")

#welcome()
#function with a parameter
def welcome(name):
    print("Welcome to Functions in python Mr.\\Ms",name)

username=input('Enter your name: \t')
#function call
# welcome(username)

#function with parameter and return

# def add(num1,num2):
#     return num1+num2

# fnum=int(input("Enter first number: \t"))
# snum=int(input("Enter second number: \t"))
# print(f'Result after adding {fnum} and {snum} is: \t',add(fnum,snum))

def multi(num1,num2):
    return num1*num2

fnum=int(input("Enter first number: \t"))
snum=int(input("Enter second number: \t"))
print(f'Result after adding {fnum} and {snum} is: \t',multi(fnum,snum))