# Assignment operators: =, +=, -=
# price=float(input("Enter Product Price"))
# discount=price*0.10
# disPrice=price-discount
# print(f"Price: {price} \n Discount {discount} \n DiscountedPrice: {disPrice}")

#salary=50000.50
#bonus=5000.60

#print(f"Salary {salary} and Bonus {bonus}")
#salary+=bonus # salary=salary+bonus
#print("Salary with Bonus", salary)

#salary=50000.50
#tds=salary*0.10
#print(f"Salary {salary} and TDS {tds}")
#salary-=tds # salary=salary-tds
#print("Salary after Tax", salary)

#Comparison Operators: ==, >, <, >=, != etc

#if(condition):
# #code
#else:
# #code

#age=int(input("Enter your Age"))
#if(age>=18):
#    print("You are eligible to cast your vote")
#else:
#    print("You are not eligible to cast your vote, You have to wait")

#print("End of the program")

#age=int(input("Enter your Age"))
#if(age>=18):
#    print("You are eligible to cast your vote")
#else:
#    print("Sorry!!! You are not eligible")

#print("End of the program")

#marks=int(input("Enter Marks percentage without '%' sign"))
#if(marks<30):
#    print("Fail in Exam")
#else:
#    print("Clear the Exam")

#accessCode="wes12"
#accessCode=input("Enter Access Code")
#if(accessCode!="wes12"):
#    print("Invalid Access Code")
#else:
#    print("Welcome to your course")

# == means equal
#accessCode=input("Enter Access Code:\t")
#if(accessCode=="wes12"):
#    print("Welcome to our course")
#else:
#    print("Invalid Access Code")

#Logical operators: and, or, not.
#phyMarks=int(input("Enter marks obtained in Physics: "))
#cheMarks=int(input("Enter marks obtained in Chemistry: "))
#mathMarks=int(input("Enter marks obtained in Mathematics: "))

#if((mathMarks>=50) and (phyMarks>=55) and (cheMarks>=60)):
#    print("You are eligible to sit in pre exam of MBBS")
#else:
#    print("You have not got the required marks")


#idProof=input("Enter ID Proof you have: ")
#if((idProof=="passport")or(idProof=="d1")or(idProof=="voter ID")):
#    print("Valid Id {idProof} we accept here")
#else:
#    print("Only passport, d1 and voter id are accepted as identity proof")
#    print(f"{idProof}: is not valid ID here")

#mathMarks=int(input("Enter marks obtained in Mathematics: "))
#gapYear=input("Enter Year gap if any otherwise 0 ")
#if((mathMarks<=55) and (gapYear !=0)):
#    print("Not eligible for BTech")
#else:
#    print("Eligible for BTech")

name=input("Enter user name: ")
if(not name):
    print("Error!!!")
else:
    print("Welcome",name)