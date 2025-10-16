numbers = [10, 25, 30, 40, 2, 1]
double_num= list(map(lambda x: 2*x, numbers))
print('Original list')
for num in numbers:
    print(num, ends=" ")

print('\nDouble) list')
for num in double_num:
    print(num,end=" ")

