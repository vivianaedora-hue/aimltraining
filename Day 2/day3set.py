# =======================================
# Set Exercises: Beginner to Advanced
# =======================================

# -----------------------------
# Beginner: Create set with duplicates and print it
# -----------------------------

numbers = {1, 2, 3, 2, 4, 3, 5}
print("Original set (duplicates automatically removed):", numbers)

print("\n")

# -----------------------------
# Intermediate: Find union and intersection of two sets
# -----------------------------

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (elements from both sets)
union_set = set1.union(set2)

# Intersection (common elements)
intersection_set = set1.intersection(set2)

print("Set1:", set1)
print("Set2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)

print("\n")

# -----------------------------
# Advanced: Print elements in set1 not in set2
# -----------------------------

set1 = {10, 20, 30, 40, 50}
set2 = {30, 50, 60, 70}

# Difference
difference_set = set1.difference(set2)

print("Set1:", set1)
print("Set2:", set2)
print("Elements in Set1 not in Set2:", difference_set)
