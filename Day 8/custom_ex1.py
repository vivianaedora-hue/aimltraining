class InvalidAge(Exception):
    pass
def check_age(age):
    if(age<=0):
        raise InvalidAge('Age should not be negative')
    if(age<18):
        raise InvalidAge('Age should be gerater than 18 years')
    if(age>=80):
        raise InvalidAge('Too old for employment')
    else:
        print(f'Age {age} is accepted and valid for employemnt')

try:
    userage=input(input('Enter your age: '))
    check_age(userage)
except InvalidAge as e:
    print('Invalid Age : ',e)    
except Exception as ex:
    print('Error!!!',ex)


    