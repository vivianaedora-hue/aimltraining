# Beginner: Create a list of numbers and print 2nd and last element

# 

#--------------------------------------------------------------------

# # Intermediate: Add, remove, and sort elements

# fruits = ["apple", "banana", "cherry"]
# print("Original list:", fruits)

# # Add element
# fruits.append("orange")
# print("After adding 'orange':", fruits)

# # Remove element
# fruits.remove("banana")
# print("After removing 'banana':", fruits)

# # Sort list alphabetically
# fruits.sort()
# print("After sorting:", fruits)

#---------------------------------------
# Advanced: Create new list with elements > 50 using list comprehension

numbers = [10, 25, 60, 45, 80, 100, 30]

# List comprehension to filter numbers greater than 50
greater_than_50 = [num for num in numbers if num > 50]

print("Original list:", numbers)
print("Numbers greater than 50:", greater_than_50)
