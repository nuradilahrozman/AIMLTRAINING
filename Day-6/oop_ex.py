# class Player:
#     def _init_(self):
#         print("Welcome to Player Class")

#     def reg(self,id,name,team):
#         self.id=id
#         self.name=name
#         self.team=team

#     def display(self):
#         print(f"ID: {self.id} \t Name: {self.name} \t Team: {self.team}")

# #object creation
# p1=Player()
# p2=Player()
# p3=Player()

# p1.reg(1,"MSD","Malaysia")
# p2.reg(2,"Chen","China")
# p3.reg(3,"Shameer","India")

# p1.display()
# p2.display()
# p3.display()


#parameterize constructor
class Player:
    def __init__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team

    def display(self):
        print(f"ID: {self.id} \t Name: {self.name} \t Team: {self.team}")
    #will use the print to call, if want to call by display use the reg
    def __str__(self):
      return f'{self.id}{ self.name}{self.team}'
#object creation
p1=Player(1,"MSD","Malaysia")
p2=Player(2,"Chen","China")
p3=Player(3,"Shameer","India")

#Display first player detail
# p1.display()
# p2.display()
# p3.display()

print(p1)
print(p2)
print(p3)