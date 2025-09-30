class employee:
    companyName="Microsoft"
    # this is the example of the class variable
    noofEmployee=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.54
        employee.noofEmployee+=1
    def showdetails(self):
        print(f"The name of the employee is {self.name} and the raise amount is {self.raise_amount} of the sized {self.noofEmployee} in the comapny {self.companyName}")
emp1=employee("MR.India")
emp1.showdetails()
emp2=employee("Conquror")
emp2.raise_amount=5.224
emp2.companyName="Google"
# this is the examle of the instance variable
emp2.showdetails()
# employee.showdetails(emp1) it is the same thing 

