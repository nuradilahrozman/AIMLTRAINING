# class Emp:
#     def display(self):
#         print("Display of Employee Class")

# obj = Emp()
# obj.display()
# #class className:
#     #defination of class
#     #attribute Method, constructors

# #objectName=ClassName()
# #ObjecrName.MethodName

# e=Emp()
# e.display()

#2nd Example
class Emp:
    def reg(self,eid,ename):
            self.eid=eid
            self.ename=ename
    def display(self):
        print("Display Details as follow")
        print("Employee Id: ", self.eid)
        print("Employee Name", self.ename)

e1=Emp()
e2=Emp()
e3=Emp()
e1.reg(1,"Dila")
e2.reg(2,"Qila")
e3.reg(3,"Mila")
print("First Employee Details")
e1.display()
print("Second Employee Details")
e2.display()
print("Third Employee Details")
e3.display()
