print('Dictionary Example')
our_dictionary=[
    {"id":'1',"name":'ravi', "age":'35'}, 
    {"id":'2',"name":'amit', "age":'30'},
    {"id":'3',"name":'vijay', "age":'35'},
    {"id":'5',"name":'nitin', "age":'12'},
    ]

for keys in our_dictionary:
    print(keys['id']+'->'+keys['name']+'->'+keys['age'])