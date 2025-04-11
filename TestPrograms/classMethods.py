class Employee:
    company="Apple"
    def __init__(self,num):
        self.num=num
    def show(self):
        print(f"{self.num}- {self.company}")
        
    @classmethod
    def changeCompany(cls,new):
        cls.company=new
print("Starting Value-",Employee.company)
e1=Employee("e1")
e2=Employee("e2")
e3=Employee("e3")
e1.show()
e2.changeCompany("Microsoft")
e2.show()
e3.show()
print("Ending Value-",Employee.company)
