# def factorial(num):
#     if(num==0)or(num==1):
#         return 1
#     else:
#         return num*factorial(num-1)
    

# num=int(input('Enter a number to find out factorial: '))
# print(f'Factorial of {num} is:',factorial(num))

#write a python function which converts inches to cm
# 1 inch =2.5 cm
def inch_to_cm(inc):
    return inc*2.5


inc=int(input('Enter inches: '))
print(f'{inc} inch are equal to {inch_to_cm(inc)} centimeter')

num=int(input('Enter inches: '))
print(f'{num} inches are equal to {inch_to_cm(num)} cm')              

#write a function to find out the table of given number
def gen_table(num):
    for i in range(1,11):
        print(f'{num}*{i}=\t{(num*i)}')

number=int(input('Enter number to find out table '))
gen_table(number)
