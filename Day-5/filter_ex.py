# #Filter()function using list [1,2,3]
# numbers=[30,23,90,60,67,99,80]

# print("Original list")
# for num in numbers:
#     print(num, end= " ")

# even_number= list(filter(lambda x: x%2==0, numbers))

# print("\nEven Numbers from lists as follow ")
# for num in even_number:
#     print(num, end=" ")

#You have the following list
# our_list=[4,2,5,6,7,3,1,10]
# #Write code using filter to find out all the numbers less than 5 from the list
# print("Original list")
# for num in our_list:
#     print(num, end= " ")

# newNum= list(filter(lambda x: x<5,our_list))

# print("\nThe list of number less than 5 is :")
# for num in newNum:
#     print(num, end=" ")

#filter using dictionary
# students_marks={"dila" :80,
#           "Mira" :70,
#           "dan" :65,
#           "tom" :39,
#           "sam" :55,
#           "yan" :22
#           }
# print("All Students")
# print(students_marks)
# pass_student=dict(filter(lambda x:x[1]>=40, students_marks.items()))  #The [1]  is referring to "dila" as 0, 80 is 1. so we only want to campare the 1 value
# print("Passed Student")
# print(pass_student)

students_marks={"dila" :75,
          "Mira" :22,
          "dan" :80,
          "tom" :39,
          "sam" :55,
          "yan" :70
          }
print("All Students")
for k,v in students_marks.items():
    print(f"Name: {k} -> marks {v}")
pass_student=dict(filter(lambda x:x[1]>=40, students_marks.items()))  #The [1]  is referring to "dila" as 0, 80 is 1. so we only want to campare the 1 value

print("Passed Student")
for k,v in pass_student.items():
    print(f"Name: {k} -> marks {v}")

sort_pass_student=dict(sorted(pass_student.items(), key=lambda x: x[1]))
print("Ascending order")
for k,v in sort_pass_student.items():
    print(f"Name: {k} -> marks {v}")

sort_pass_student_desc=dict(sorted(pass_student.items(), key=lambda x: x[1], reverse=True))
print("Descending order")
for k,v in sort_pass_student_desc.items():
    print(f"Name: {k} -> marks {v}")