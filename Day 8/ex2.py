from ourpack import calc
while True:  # loop to allow continuous use
    try: 
        fnum=float(input('Enter first number: '))
        snum=float(input('Enter second number: '))
        op=input('Choose operation +,-,*,/ : ')
        if(op=='+'):
            print('Result: \t',calc.add(fnum,snum))
        elif(op=='-'):
            print('Result: \t',calc.sub(fnum,snum))
        elif(op=='*'):
            print('Result: \t',calc.multi(fnum,snum))
        elif(op=='/'):
            print('Result: \t',calc.div(fnum,snum))
        else:
            raise ValueError   # OR print('Wrong operation choice')
    except ZeroDivisionError as ze:
        print('Division by 0 not allowed',ze)
    except ValueError as ve:
        print('Error in values',ve)
    except Exception as ex:
        print('Error!!!',ex)
    choice=input('Do you want to continue if yes press y: \t').lower() #lower() use to chnage the CAPS LOCK into small case
    if choice!='y':
        print('Bye')
        break

# finally:
#     print('End of program')