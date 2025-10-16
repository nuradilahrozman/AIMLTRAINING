# def factorial(num):
#     if(num==0) or (num==1):
#         return 1
#     else:
#         return num*factorial(num-1)
# num=int(input("Enter a number to find out the factorial: "))
# print(f"Factorial of {num} is : {factorial(num)}")
    

# def factorial(num):
#     while True:

#         if(num==0) or (num==1):
#             return 1
#         else:
#          return num*factorial(num-1)

# num=int(input("Enter a number to find out the factorial: "))
# print(f"Factorial of {num} is : {factorial(num)}")
    
#Exercise
#write a function which converts inches to cms. 1inch= 2.5cm

def convert(inch):
    return inch*2.5
inch=float(input("please enter the inch to convert :"))
print(f"{inch}inch if convert to cm is :",convert(inch),"cm")


