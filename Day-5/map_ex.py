#map()function using list [1,2,3]
numbers=[30,20,90,60]
double_num= list(map(lambda x: 2*x,numbers))
#print(double_num)# on way
print("Original list")# 2nd way
for num in numbers:
    print(num, end= " ")

print(" \nDouble list")
for num in double_num:
    print(num, end=" ")

#Filter()function using list [1,2,3]
