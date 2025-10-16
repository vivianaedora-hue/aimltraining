# employee={"id":1,
#           "name":"Sam",
#           "salary":55000.50
#           }

# print("Employees details as follows:")
# for key, value in employee.items():
#     print(key,"->",value)
# #adding key in dictionary
# employee["city"]="Muscat"
# print('\nDictionary after adding City\n')

# for key, value in employee.items():
#     print(key, "->", value)

# del employee["salary"]
# print("\nDictionary after deleting Salary\n")
# for key, value in employee.items():
#     print(key, "->", value)
employee={"id":1,
          "name":"Sam",
          "salary":55000.50
          }
print('All keys from employee ')
for k in employee.keys():
    print(k,end="\t")

print('\nAll values from employee')
for v in employee.values():
    print(v,end="\t")

print('\nKey:Value')
for k,v in employee.items():
    print(k," :",v)

print('\nDictionary as follows')
print(employee)
del employee["salary"]
print('After deleting Salary')
for k,v in employee.items():
    print(k," :",v)