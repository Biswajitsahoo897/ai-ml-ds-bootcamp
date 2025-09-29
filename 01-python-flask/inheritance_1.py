class employee:
    def __init__(self,name, id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"The name of the employee id {self.id} is {self.name}.")
class programmer(employee):
    def showlanguage(self):
        print("The default langauge is pyhton")        


emp1=employee("Binaya",421)
emp1.showdetails()
emp2=employee("Mamata",451)
emp2.showdetails()
# emp2=programmer(9,4)
emp2.showlanguage()

# this is the example of the class variable
class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        

obj1 = MyClass()
obj2 = MyClass()

obj1.print_class_variable() # Output: 2
obj2.print_class_variable() # Output: 2


# this is the example of the instance var

class MyClass:
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)
        
obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name() # Output: John
obj2.print_name() # Output: Jane