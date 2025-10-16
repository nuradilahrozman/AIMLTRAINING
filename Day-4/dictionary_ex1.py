# employee={"id": 12,
#           "name":"Dila",
#           "salary": 3000}
# print("Employees Details as follows:")
# for key,value in employee.items():
#     print(key,":", value)

# #Adding key in dictionary
# employee["city"]="muscat"
# print("\nDictionary after adding city\n")

# for key,value in employee.items():
#     print(key,":", value)

# #Delete key in dictionary
# del employee["salary"]
# print("\nDictionary after remove salary\n")

# for key,value in employee.items():
#     print(key,":", value)


#Key
employee={"id": 12,
          "name":"Dila",
          "salary": 3000}

print("All keys from Employee")
for k in employee.keys():
    print(k,end=" ")
#values
print("\nAll values from Employee")
for v in employee.values():
    print(v,end=" ")
#another way of display
print ("\nkey : values")
for v,k in employee.items():
    print(k, ":" ,v)

print("\nDictionary as follows")
print(employee)
del employee["salary"]
print("After deleting salary")
for k,v in employee.items():
    print(k, ":",v)