class Employee:
    company="DELL"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method (by default)
    def print_info(self):
        info=f"Name is {self.name} and salary is {self.salary} in {Employee.company}"
        return info
    # Regular method 
    # def sum(a,b):
    #     return a+b

    # Static method
    @staticmethod # It does not take self or cls as the first argument
    def sum(a,b):
        return a+b
    
    # Class method
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
    # Class method
    @classmethod
    def print_company(cls):
        return cls.company

e1=Employee("Biswajit", 100000)
e2=Employee("John", 200000)

# print(Employee.company)
# print(Employee.name) #this will give error because name is not a class variable
# print(e1.print_info())
# print(e1.sum(5,6))
# Method inside a class is called an instance method
# because it is called by an instance of the class

print(e1.print_company())
e1.change_company("Apple")
print(e1.print_company())
print(Employee.company) # hence company is changed for all the instances of the class
