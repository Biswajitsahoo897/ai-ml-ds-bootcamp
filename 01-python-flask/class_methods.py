class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany
        # by using the class methods we can change the company name by overcoming instance variable 
        # To define a class method, you simply use the
        # "@classmethod" decorator before the method definition. The
        # first argument of the method should always be "cls,"which
        # represents the class itself. Here is an example of how to
        # define a class method:

        # we can write whatever we want in the cls  but make sure that object of the paramenter is same

e1 = Employee( )
e1.name = "conquror"
e1. show( )
e1. changeCompany("Microsoft")
e1. show( )
print(Employee.changeCompany("adobe"))
print(Employee.company)