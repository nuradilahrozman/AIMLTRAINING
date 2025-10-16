# print("We are going to discuss about tuple :)")
#A tuple is an immutable data type in python. Once created, values cannot be changed

# subject=("python","java","dotnet","sql","power bi")
# print("All subject are :")
# print("Number of subjects are : ",len(subject))
# for sub in subject:
#     print(sub,end=" ")

# numbers=(1,2,3,4,10,2,3,2,3,5,50,1)
# print("Total Number in tuple:",len(numbers))
# for num in numbers:
#     print(num,end=" ")

#tupleName.index (item) will return the index of first occurrence of item in tupleName.
# search_num=int(input("Enter Number to find out index: "))
# if search_num in numbers:
#     print(f"Index of {search_num} is: \t",numbers.index(search_num))
# else:
#     print(f"No such number{search_num}in our list")

#tupleName.count (item):  a count (item) will return number of times item occurs in tupleName.
# search_num=int(input("Enter Number to find out frequency: "))
# if search_num in numbers:
#     print(f"number {search_num} frequency is:  {numbers.count(search_num)} times")
# else:
#     print(f"No such number{search_num}in our list")

#Task - Write a program to sum a list with 4 numbers.
Number=[67,50,40,33]
result=sum(Number)
print(f"The total of the list is ",result)

#Task - Write a program to sum a tuple with 4 numbers.
Number=(67,50,40,33)
result=sum(Number)
print(f"The total of the list tuple is ",result)
