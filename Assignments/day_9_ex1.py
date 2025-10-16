# Write a program using functions to find greatest of three numbers entered by user
# Write the solution in Assignments folder with name
# day_9_ex1.py
# Push on GitHub
# Share GitHub link in chat once done

def find_greatest(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# Main program
print("Enter three numbers:")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

greatest = find_greatest(a, b, c)
print("The greatest number is:", greatest)


