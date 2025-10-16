# import random
# print('Random number from 1 to 1000')
# print(random.randint(1,1000))

import random
def findwinner():
    name=input('Enter your name: ')
    luckyNumber=random.randint(1,10)
    print(f'Welcome Mr.\\Ms. {name} coupon number: {luckyNumber}')
    if(luckyNumber==1):
        print('you have won Proton XL-65')
    elif(luckyNumber==3):
        print('you have won a Ipad')
    elif(luckyNumber==9):
        print('you have won an Iphone')
    else:
        print('Better luck next time')