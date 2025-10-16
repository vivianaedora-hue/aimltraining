# print("List Example One")

# my_list = [10,20,30, "Python",None, True, 12.45,'Ravi']
# print('Number of items in list are:', len(my_list))

# for item in my_list:
#     print(item)

# print("Second Example of List")
# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of Employees:",len(emps))
# print('Áll Employees')
# # for emp in emps:
# #     print(emp)

# #print(emps)

# for emp in emps:
#     print(emp,end=" ")


# #Sort Example
# #listName.sort()
# emps.sort()
# print("\n List after sorting")
# for e in emps:
#     print(e, end="")
    
#     #Reverse example
#     #listName.reverse()
# emps.reverse()
# print('\n Employees in descending order')
# for e in emps:
#     print(e, end=" ")

#append,remove,pop insert method

# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of Employees:",len(emps))
# for emp in emps:
#     print(emp,end=" ")

    #append :   adds the item at the end of the list
# newEmp=input("\nEnter employee name to add in list:\t")
# emps.append(newEmp)
# print('\nAfter adding new employee: Number of employees are:',len(emps))
# for emp in emps:
#     print(emp, end=" ")

#insert(index,item): This will add item at given index
# newEmp=input("\nEnter employee name to add in list:\t")
# pos=int(input("Enter position where you want to insert inside list:\t"))
# emps.insert(pos,newEmp)
# print('\nAfter adding new employee: Number of employees are:',len(emps))
# for emp in emps:
#     print(emp, end=" ")

# #append,remove,pop insert method

# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of Employees:",len(emps))
# for emp in emps:
#     print(emp,end=" ")
#listName.remove9item): Will remove the item from list
# delEmp=input('Employee to remove from list:\t')
# if delEmp in emps:
#     emps.remove(delEmp)
#     print(f"Number of employees after deleting {delEmp} in list are:",len(emps))
#     for emp in emps:
#         print(emp, end=" ")
# else:
#     print(f'No such item {delEmp} in emplyee list')

#pop() example
#listName.pop(index): removes the item from given index and returns the value
# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of Employees:",len(emps))
# for emp in emps:
#     print(emp,end=" ")

# del_index=int(input('Enter index to pop item:\t'))
# print('Pop result: ',emps.pop(del_index))

# print("Number of employees after pop() are:",(len))
# for emp in emps:
#     print(emp, end=" ")

#find out first and last element from the list'
emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
print("Number of Employees:",len(emps))
for emp in emps:
    print(emp,end=" ")
count=len(emps)
print('\n First element of Employee list is: ',emps[0])
print('\n Last element of Employee list is: ',emps[-1])
print('\n second Last element of Employee list is: ',emps[-2])
print('\n Last element of Employee list is: ',emps[count-1])
