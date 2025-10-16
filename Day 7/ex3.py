import datetime
import inspect 
dtclassess =inspect.getmembers(datetime, inspect.isclass)

print('All clasess in datetime module')
for n, func in dtclassess:
    print(n,end="\t")

print('\n ---Today ---\n')
print(datetime.date.today())

print('\n ---Current Time ---\n')
print(datetime.datetime.now())
print('\n ---Current Time ---\n')
print(datetime.datetime.now().time())
print(datetime.datetime.now().time())

cttime=datetime.datetime.now.time
formattedtime=datetime.time.now().strftime('%I %M %S %p')

print ('Curent time',cttime)
print ('Formatted time',formattedtime)
