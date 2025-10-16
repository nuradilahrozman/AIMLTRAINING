## Assignment operators: =,+=, -=
# price=float(input("Enter Product price \t"))
# discount=price*0.10
# disPrice=price-discount
# print(f"Price: {price} \n Discount {discount} \n Discounted Price {disPrice}") # \n is new line

# salary=50000.50
# bonus=5000.60
# print(f"Salary {salary} and Bonus {bonus}")
# salary+=bonus #salary=salary+bonus
# print("Salary with Bonus",salary)

# salary=50000.50
# tds=salary*0.10
# print(f"Salary {salary} and TDS {tds}")
# salary-=tds #salary=salary-tds
# print("Salary after tax",salary)

##Comparison operator : ==,>,>=,<,!=

#if(condition):
# code
# else :
# code

# age=int(input("Enter you age "))
# if(age>=18):
#     print("You are eligible to vote")
# else:
#     print("you are no eligle to cast your vote, you have to wait")
# print("End of program")

# marks=int(input("Enter mark percentage without '%' sign: "))
# if(marks<30):
#     print("Failed in exam!")
# else:
#     print("Pass the exam!")

# #accesscode="lalacan" (!= , not equal to)
# Accesscode=input("Please Enter the code :")
# if(Accesscode!="lalacan"):
#     print("Invalid code, Try again")
# else:
#     print("Welcome to the course :)")

#     #accesscode="lalacan" (== , equal to)
# Accesscode=input("Please Enter the code :")
# if(Accesscode =="lalacan"):
#      print("Welcome to the course :)")
# else:
#     print("Invalid code, Try again")

##Logical operator - and / or / not
# phyMarks=int(input("Enter you Physic Marks "))
# cheMarks=int(input("Enter you Chemistry Marks "))
# MathMarks=int(input("Enter you Mathematics Marks "))

# if((MathMarks>=55) and(phyMarks>=50) and (cheMarks>=60)):
#     print("You are eligible to sit in pre exam of MBBS")
# else:
#     print("You did not get the required marks")


# idproof=input("Enter Id Proof you have ")
# if((idproof=="passport")) or (idproof=="dl") or (idproof=="voter id"):#either one true then its true
#     print(f"Value Id{idproof} we accept here")
# else:
#     print("Only passport, dl and voter are accepted as I dentity proof")
#     print(f"{idproof} : is not valid ID here")


# MathMarks=int(input("Enter you Mathematics Marks "))
# gapYear=int(input("Enter Year gap if any otherwise 0 :"))

# if((MathMarks>=55) or (gapYear!=0)):
#     print("You are not eligible for BTech")
# else:
#     print("You are eligible for BTech")

name=input("Enter user name")
if(not name):
    print("Error")
else:
    print("Welcome",name)