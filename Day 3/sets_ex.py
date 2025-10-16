# print("Sets in Python")
# set_one={'laptop','airphone','ipad','mobile','headphone','laptop','ipad'}
# print('Number of items in set_one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")

#clear(): remove all the items from set

# set_one.clear()
# print('\nAfter clear() method, number of items in set_one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")
#---------------------------------
# set_one={'laptop','airphone','ipad','mobile','headphone','laptop','ipad'}
# print('Number of items in set_one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")
# #set.remove(item): updates thes set and removes item from set
# set_one.remove('airphone')
# print('\n after removing pne item from set :',len(set_one))
# for item in set_one:
#     print(item,end=" ")

#union,intersection,difference
# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300}
# set_three={5000,11000}
# #union
# #s1.union(s2): returns a new set with all items from both sets s1,s2
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# unionset=set_one.union(set_two,set_three)
# print(f'Union of set_one, set_two and set_three contains: {len(unionset)} following items')


# print(unionset)

#union,intersection,difference
set_one={100,200,300,500,700,900,150}
set_two={100,400,700,1000,1300}
#intersection example
#s1.intersection(s2): returns set which contains only items from both sets s1,s2
print(f'set_one contains: {len(set_one)} items')
print(set_one)
print(f'set_two contains: {len(set_two)} items')
print(set_two)
newset=set_one.intersection(set_two)
print(f'Union of set_one, set_two and set_three contains: {len(newset)} following items')
print(newset)

set_one={100,200,300,500,700,900,150}
set_two={100,400,700,1000,1300}
#intersection example
#s1.intersection(s2): returns set which contains only items those in sets s1,but not in s2
print(f'set_one contains: {len(set_one)} items')
print(set_one)
print(f'set_two contains: {len(set_two)} items')
print(set_two)
newset=set_one.difference(set_two)
print(f'difference of set_one, set_two contains: {len(newset)} following items')
print(newset)