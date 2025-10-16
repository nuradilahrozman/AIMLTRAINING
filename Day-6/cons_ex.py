class EMP:
    def __init__(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=qual
        
    def display(self):
        print("Id: ", self.id)
        print("Name : ", self.name)
        print("Qual :", self.qual)

class Dev(EMP):
    def __init__(self, id, name, qual,domain,project):
        super().__init__(id, name, qual)
        self.domain=domain
        self.project=project

    def display(self):
        super().display()
        print("Domain: " ,self.domain)
        print("Project: ",self.project)

#create one Emp object with id=1,name="Dila",qual="MCA"
emp=EMP(1,"Dila","MCA")

#Create one Dev object with id=3, name, "Ravi", qual="Mtech", project="eShopping", Domain="dot net"
dev=Dev(3,"Ravi","Mtech","eshoping","dot net")

# Display Dev Details
print("Developer detail as follow")
dev.display()
#Display details
print("Employee Details as follow")
emp.display()