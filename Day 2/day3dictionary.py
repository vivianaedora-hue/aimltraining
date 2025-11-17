# Beginner: Create dictionary and print key-value pairs

# student = {
#     "name": "Alice",
#     "age": 20,
#     "course": "Python"
# }

# print("Student details:")
# for key, value in student.items():
#     print(key, ":", value)


# Intermediate: Add new key and delete another

employee ={
    "id":1,
    "name": "John",
    "department": "HR",
    "salary": 50000,
    
}

print("Original Dictionary:", employee)
print("Employee Details:")
for key, value in employee.items():
    print(key, ":", value)
# Add new key
employee["location"] = "New York"

# Delete key
del employee["department"]

print("Updated Dictionary:", employee)

for key, value in employee.items():
    print(key, ":", value)

# Advanced: Find student with highest marks from dictionary

# marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 95,
#     "Emma": 88
# }

# # Find student with max marks
# top_student = max(marks, key=marks.get)

# print("Marks:", marks)
# print("Top student:", top_student, "with marks", marks[top_student])
