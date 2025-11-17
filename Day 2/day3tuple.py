# =======================================
# Tuple Exercises: Beginner to Advanced
# =======================================

# -----------------------------
# Beginner: Print subjects from tuple
# -----------------------------

subjects = ("Math", "Science", "History", "English")
print("Subjects in the tuple:")
for subject in subjects:
    print(subject)

print("\n")

# -----------------------------
# Intermediate: Find index of a given value
# -----------------------------

fruits = ("apple", "banana", "cherry", "orange", "banana")
index_value = fruits.index("cherry")

print("Tuple:", fruits)
print("Index of 'cherry':", index_value)

print("\n")

# -----------------------------
# Advanced: Count frequency of each number in a tuple
# -----------------------------

numbers = (10, 20, 10, 30, 20, 40, 10, 30)
frequency = {num: numbers.count(num) for num in set(numbers)}

print("Original tuple:", numbers)
print("Frequency of each number:", frequency)
