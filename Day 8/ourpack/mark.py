class InvalidMarks(Exception):
    pass

def check_marks(marks):
    if (marks<0):
        raise InvalidMarks("Marks cannot be negative.")
    elif (marks>50):
        raise InvalidMarks("Marks cannot exceed 50.")
    else:
        print(f" Marks {marks} accepted as valid.")