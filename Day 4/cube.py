#print('Write a function to findout the cube of given number')
#5  : 5*5*5 (e.g cube of 5 is 5*5*5 means 125)

# def cube(num):
#     return num*num*num
# num=int(input('Enter a number to find its cube:\t'))
# print(f'Cube of {num} is:\t',cube(num))

#Write a functon to calculate bonus of given salary
#function take salary as input and return bonus (10% of salary)

#Option 1
# print('Welcome to salary calculator')
# def bonus(sal):
#     return (sal*10)/100
# sal=float(input('Enter your salary:\t'))
# num=int(input('Enter bonus percentage:\t'))
# print(f'Your {num}% bonus is:\t',bonus(sal))

#Option 2
def calc_bonus(salary):
    return salary*0.10

salary=float(input('Enter your salary to find out bonus:\t'))
print(f'Your salary is: {salary} bonus is:\t',calc_bonus(salary))            