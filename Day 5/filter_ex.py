# numbers = [10, 25, 30, 40, 2, 1]

# print('Original list')
# for num in numbers:
#     print(num, end=" ")

# even_numbers=list(filter(lambda x: x%2==0, numbers))

# print('\nEven numbers from list as follows')
# for num in even_numbers:
#     print(num,end=" ")

#you have following list
our_list=[4,2,5,6,7,3,1,10]
#write code using filter to find out all number less than 5
#   from the list
our_numbers= list(filter(lambda x: x<5, our_list))

print('Original list')
for num in our_list:
    print(num, end=" ")

print('\n New list as follows\n')
for num in our_numbers:
    print(num, end=" ")

students_marks={'Sam':60,
                'Raj':55,
                'Mihir':35,
                'Sandy':45,
                'Niraj':76,
                'Deep':40,
                'Garima':54
                }
print('All students')
for k,v in students_marks.items():
    print(f'Name: {k} -> Marks {v}')

pass_students=dict(filter(lambda i:i[1]>=50, students_marks.items()))

print('Passed student')
for k,v in pass_students.items():
    print(f'Name: {k} -> Marks {v}')

sort_pass_students=dict(sorted(pass_students.items(), key=lambda x: x[1]))
print('Ascending order')
for k,v in pass_students.items():
    print(f'Name: {k} -> Marks {v}')

sort_pass_students_desc=dict(sorted(pass_students.items(), key=lambda x: x[1],reverse=True))

print('Descending order')
for k,v in sort_pass_students_desc.items():
    print(f'Name: {k} -> Marks {v}')
