#def function_name(parameter)
#   '''Docstring'''
#   statement(s)

#Function without parameter
# def welcome():
#     print("Welcome to Function")

# #Function call.can call how many time you want.
# welcome()
# welcome()

#Function with a parameter
# def welcome(name):
#     print("Welcome to function in python Mr.\Mrs",name)
# username=input("Enter you name :")
    
# welcome(username)

#Function with parameter and return

# def add(num1,num2):
#     return num1+num2
# fnum=int(input("Enter first number "))
# snum=int(input("Enter second number "))
# print(f"Result after adding {fnum} and {snum} is = ",add(fnum,snum))

#Multiply
def multi(num1,num2):
    return num1*num2
fnum=int(input("Enter first number "))
snum=int(input("Enter second number "))
print(f"Result after adding {fnum} and {snum} is = ",multi(fnum,snum))