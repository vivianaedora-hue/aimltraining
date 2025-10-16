#Take user marks from user with in 0 to 50
#if user enter outside [0-50] raise Error InvalidMarks using Custom Exception
#Give chance to the user till , he/she entered valid marks

# Custom exception class
class InvalidMarks(Exception):
    pass

def check_marks(marks):
    if (marks<0):
        raise InvalidMarks("Marks cannot be negative.")
    elif (marks>50):
        raise InvalidMarks("Marks cannot exceed 50.")
    else:
        print(f" Marks {marks} accepted as valid.")

# Keep asking user until valid marks are entered
while True:
    try:
        marks =int(input("Enter your marks (0–50): "))
        check_marks(marks)
        # Exit loop once marks are valid
    except InvalidMarks as e:
        print("Invalid Marks:", e)
    except Exception as ex:
        print("Unexpected Error:", ex)
    else:
        print('Recorded')
        break
    
    choice=input('Do you want to re-enter marks? If yes, press y: \t').lower()
    if(choice!='y'):
        break
