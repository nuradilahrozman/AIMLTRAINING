#While Loop
# ourNum=1
# print("Print Numbers from 1 to 100")
# while(ourNum <=100):
#     print(ourNum,end=" ")
#     ourNum+=1

#Break loop
ourNum=1
# print("Print Numbers from 1 to 100 before we get the numbers divisible 11")
# while(ourNum <=100):
#     if(ourNum%11==0):
#         break
#     print(ourNum,end=" ")
#     ourNum+=1

#continue example
# ourNum=1
# print("Print Numbers from 1 to 100 those are not divisible 11")
# while(ourNum <=100):
#     if(ourNum%11==0):
#         ourNum+=1
#         continue
#     print(ourNum,end=" ")
#     ourNum+=1 

#continue example
# print("Print odd number form 1 to 100")
# num=1
# while(num<=100):
#     if(num%2==0):
#         num+=1
#         continue
#     print(num,end= " ")
#     num+=1

# for i in range(1,100):
#     if(i%5==0):
#         continue
#     print(i,end=" ")

# when to use "for loop" and "while loop" - for loop- we use when we know the condition.If we dont know the condition/how many to loop we use while loop 

#not really looping
# Correctpwd="1234"
# pwd=input("Enter Password to start the Game ")
# while True:
#     if(Correctpwd==pwd):
#         print("Welcome, Access Granted")
#         print("***Game start***")
#         break
#     else:
#         print("Wrong Password, Try Again")
#         break

#this one correct - baru looping
Correctpwd="1234"
counter=0
while True:
    pwd=input("Enter Password to start the Game ")
    if(Correctpwd==pwd):
        print("Welcome, Access Granted")
        print("***Game start***")
        break
    else:
        print("Wrong Password, Try Again")
        counter+=1
        if(counter>=3):
            print("Too many attempts")
            print("Please try again after 10 mins")
            break
       
        
        
       
     