# class account:
#     def __init__(self, ac_holder,bal):
#         self.ac_holder=ac_holder
#         self.bal=bal

#     def deposit(self, amount):
#         self.bal+=amount
#         print("Balance after deposit",self.bal)

#     def withdraw(self,amount):
#         if(self.bal>=amount):
#          self.bal-=amount
#          print("Balance after withdraw:",self.bal)
#         else:
#            print("Insufficient amount in account")
#            print("Transaction Failed")

#     def show(self):
#        print(f"Account Holder Name : {self.ac_holder} Acccount Balance {self.bal}")

# #TO DISPLAY THE DEF SHOW
# # ac1=account("Dila", 70000)
# # ac2=account("Faiz", 80000)
# # ac1.show()
# # ac2.show()

# ac1=account("Dila", 8000)
# ac1.show()
# wamount=float(input("Enter amount to withdraw "))
# ac1.withdraw(wamount)


# class Account:
#     def __init__(self,balance,ac_holder):
#         self.balance=balance
#         self.ac_holder=ac_holder


#     def get_balance(self):
#         return self.balance
    
# acc=Account(10000, "Dila")
# acc.balance=34000
# print(acc.balance)

#EXAMPLE 3
class account:
    def __init__(self, ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal

    def deposit(self, amount):
        self.bal+=amount
        print("Balance after deposit",self.bal)

    def withdraw(self,amount):
        if(self.bal>=amount):
         self.bal-=amount
         print("Balance after withdraw:",self.bal)
        else:
           print("Insufficient amount in account")
           print("Transaction Failed")

    def show(self):
       print(f"Account Holder Name : {self.ac_holder} Acccount Balance {self.bal}")


ac=account("Dila", 80000)
ac.show()
print("Please choose 1.Deposit 2.Witthdraw 3,Balance Info")
Trans=int(input())#first way
#Trans=int(input("Please enter 1 or 2 : ")) #2nd way
if(Trans==1):
   Damount=float(input("Enter amount to Deposit "))
   ac.deposit(Damount)
elif(Trans==2):
   wamount=float(input("Enter amount to withdraw "))
   ac.withdraw(wamount)
elif(Trans==3):
    ac.show()
else:
    print("Wrong choice")

   

