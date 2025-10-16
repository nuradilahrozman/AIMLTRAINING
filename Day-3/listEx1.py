# print("List Example One")

# my_list = [10, 20, 30, "Python", None, True, 12.43, "Ravi"]
# print("Number of item in list are:",len(my_list)) #len is to know the total of my_list
# for item in my_list:
#     print(item)

# print("Second Example of List")
# emps=["Dila","Mira","Qila","Ani","Tiqah","Syera","Fiha"]
# print("Number of Employees",len(emps))
# print("All Employee")

# #firstway
# # for emp in emps:
# #     print(emp) # will appear next line, next line

# #2nd way
# #print(emps) #will appaer exactly as the emps= that we create

# #3rd way
# for emp in emps:
#     print(emp,end=" ") # will appear in one line with space

#Sort Example (Ascending order)
#list_name.Sort()
# emps.sort()
# print("\nList after sorting")
# for e in emps:
#     print(e,end=" ")

#Sort Example (descending order)
#list_name.reverse()
# emps.reverse()
# print("\nList after sorting in descending order")
# for e in emps:
#     print(e,end=" ")


#append,remove,pop insert method
emps=["dila","mira","qila","ani","tiqah","syera","fiha"]
print("Number of Employees",len(emps))
for emp in emps:
    print(emp,end=" ")

#append : adds the item at the end of list
# newEmp=input("\nEnter Employess name to add in the list :")
# emps.append(newEmp)
# print("\nAfter adding New Employee: Number of Employees are :",len(emps))
# for emp in emps:
#     print(emp,end=" ")

#Insert(index,item):This will add item at given index
# newEmp=input("\nEnter Employess name to add in the list: ")
# pos=int(input("\nEnter position where you want to insert inside list: "))
# emps.insert(pos,newEmp)
# print("\nAfter adding New Employee: Number of Employees are :",len(emps))
# for emp in emps:
#     print(emp,end=" ")

#Remove(item) : will remove item from the list
# delEmp=input("\nEmployee to remove from the list: ")
# if delEmp in emps:
#     emps.remove(delEmp)
#     print(f"Number of Employees after deleting {delEmp} in the list are:",len(emps))
#     for emp in emps:
#         print(emp,end=" ")
# else:
#     print(f"No such item {delEmp} in employee list")

#POP(index): will delete element at given index and return its value
# del_index=int(input("\nEmployee to remove from the list: "))
# print("Pop Result: ",emps.pop(del_index))
# print("Numberof Employees after pop() are :",len(emps))
# for emp in emps:
#     print(emp,end=" ")

#Find out first and last element from the list
# print("First Element of employee list is : ",emps[0])
# print("Last Element of employee list is : ",emps[-1])




