# def add(num1,num2):
#     return num1+num2

# def multi(num1,num2):
#     return num1*num2

# def avg(num1,num2):
#     return (num1+num2)/2

# def sub(num1,num2):
#     return num1-num2

# def div(num1,num2):
#     return num1/num2
# print("Welcome to our calculator")
# while True:
#     print("Select Operation \n1.Add \n2.Sub \n3.Multi \n4.Division \n5.Average \n6.Exit")
#     op=int(input("Enter your Operation choice (1-6): "))
#     if(op==6):
#         print("Byeeeeeeee")
#         break
#     if(op>=6) or (op<=0):
#         print("Wrong operation choice, please choose only 1 to 6")
#         break
#     fnum=float(input("Enter first number: "))
#     snum=float(input("Enter second number: "))
#     if(op==1):
#         print(f"Result after adding {fnum} and {snum} is ",add(fnum,snum))
#     elif(op==2):
#         print(f"Result after multi {fnum} and {snum} is ",multi(fnum,snum))
#     elif(op==3):
#         print(f"Result after avg {fnum} and {snum} is ",avg(fnum,snum))
#     elif(op==4):
#         print(f"Result after sub {fnum} and {snum} is ",sub(fnum,snum))
#     elif(op==5):
#         print(f"Result after div {fnum} and {snum} is ",div(fnum,snum))
    

def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def avg(num1,num2):
    return (num1+num2)/2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2
print("Welcome to our calculator")
while True:
    print("Select Operation \n1.Add \n2.Sub \n3.Multi \n4.Division \n5.Average \n6.Exit")
    op=int(input("Enter your Operation choice (1-6): "))
    if(op==6):
        print("Byeeeeeeee")
        break
    if(op>=6) or (op<=0):
        print("Wrong operation choice, please choose only 1 to 6")
    else:
        fnum=float(input("Enter first number: "))
        snum=float(input("Enter second number: "))
        if(op==1):
            print(f"Result after adding {fnum} and {snum} is ",add(fnum,snum))
        elif(op==2):
            print(f"Result after multi {fnum} and {snum} is ",multi(fnum,snum))
        elif(op==3):
            print(f"Result after avg {fnum} and {snum} is ",avg(fnum,snum))
        elif(op==4):
            print(f"Result after sub {fnum} and {snum} is ",sub(fnum,snum))
        elif(op==5):
            print(f"Result after div {fnum} and {snum} is ",div(fnum,snum))
    
