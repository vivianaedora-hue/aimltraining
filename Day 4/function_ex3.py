#default parameter in functions
# def info(id,name,city='KL'):
#     print(f"Details as follows \n ID: {id} Name: {name} City: {city}")


# info(1,'Sam','New Delhi')
# info(101,'Xi')
# info(103,'Chang')
# we want to create a single method that can able to add 2, 3 numbers, 3 numbers, 4 numbers, or 5 numbers
# and return correct total

# def add(n1,n2=0,n3=0,n4=0,n5=0):
#     return n1+n2+n3+n4+n5

# print("Result: ",add(1,2))
# print("Result: ",add(5,3,1,4,10))
# print("Result: ",add(5,25,10))

# def add(*nums)
#     return sum(nums)

# print('Sum of 1,10,11 is: \t',add(1,10,11))
# print('Sum of 5,2,is: \t',add(5,2))
# print('Sum of 10,10,100,100,200,219,19 is: \t',add(10,10,100,100,200,219,19))


print('Maximum example')
print('Maximum of 1,10,11 is: \t',max(1,10,11))
print('Maximum of 5,2,is: \t',max(5,2))
print('Maximum of 10,10,100,100,200,219,19 is: \t',max(10,10,100,100,200,219,19))

print('Minimum example')
print('Min of 1,10,11 is: \t',min(1,10,11))
print('Min of 5,2,is: \t',min(5,2))
print('Min of 10,10,100,100,200,219,19 is: \t',min(10,10,100,100,200,219,19))

