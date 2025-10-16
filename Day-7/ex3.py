import datetime
import inspect
dtclasses= inspect.getmembers(datetime, inspect.isclass)

print('All Classes in datetime module')
for n, func in dtclasses:
    print(n, end=" ")

print('\n.........Today...........')
print(datetime.date.today())

print('......Current Time.......')
print(datetime.datetime.now())

print('......Current Time.......')
print(datetime.datetime.now().time())
print(datetime.datetime.now().time())

cttime=datetime.datetime.now().time()
formatedtime=datetime.datetime.now().strftime('%I:%M:%S:%P')

print('Current time', cttime)
print('Formated time',formatedtime)

