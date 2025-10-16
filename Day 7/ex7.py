# try:
#     num1=int(input('Enter first number'))
#     num2=int(input('Enter second number'))
#     total=num1+num2
#     print(f'Sum of {num1} and {num2} = {total}')
# except Exception as e:
#     print('Error',e)
# finally:
#     print('End of program')

try:
    num1=int(input('Enter first number'))
    num2=int(input('Enter second number'))
    div=num1/num2
    print(f'Result after dividing {num1} by {num2} = {div}')
except Exception as e:
    print('Error',e)
finally:
    print('End of program')