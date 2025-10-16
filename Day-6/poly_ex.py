# class Bird:
#     def fly(self):
#         print("Bird can fly")

# class Airplane(Bird):
#     def fly(self):
#         print("Airplane fly")

# b=Bird()
# print("Bird Implement")
# b.fly()

# print("Airplane Implemenatation")
# a=Airplane()
# a.fly()
# print("using for loop")
# for obj in [Bird(), Airplane()]:
#     obj fly()

class EMP:
    def reg(self):
        self.id=int(input("Enter Id "))
        self.name=(input("Enter Name "))

    def disp(self):
        print("Name: ", self.name)
        print("Id : ", self.id)

class Dev(EMP):
    def reg(self):
        super().reg()
        self.domain=("Enter Domain")

    def disp(self):
        super().disp()
        print("Domain: ", self.domain)
    
    
d1=Dev()
d1.reg()
d1.disp()
