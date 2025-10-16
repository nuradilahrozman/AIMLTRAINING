# import math
# import random
#my_num=int(input("Enter number to find out square root "))
#print(f"square root of{my_num} is : ", math.sqrt(my_num))

#print("Your lucky Number from 1 to 100 is ", random.randint(1,100))

#To check function inside module
import math
import inspect
#print(math.sin(45)) #ex can do this too.one line only
# #Get only function defined in the math module
function = inspect.getmembers(math, inspect.isbuiltin)

# #Display function names
for n, func in function: #one way to display
     print(n)
# print(function)#2nd way

print("sin 90 is:", math.sin(90))
print("cos 90 is: ",math.cos(90))
print("Tan 90 is: ",math.tan(90))

deg=int(input("Degree to find out cos"))
print("COS{deg} is :",math.cos(deg))

