#import math
# num=int(input("Enter number to find out square root "))
# print(f'square root of {num} is : ',round( math.sqrt(num),2)) # round (      ,2) is to round up to 2 decimal point
# #print(math.sqrt(64))# gini pun bolehh

import math
import inspect
function = inspect.getmembers(math, inspect.isbuiltin)
print("All Function in math module")
for n, func in function:
    print(n, end=" ")