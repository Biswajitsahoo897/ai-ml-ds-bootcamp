# Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method 
# in a derived class. The method in the derived class is said to override the method in the base class. 
# When you create an instance of the derived class and call the overridden method, the version of the method in
#  the derived class is executed, rather than the version in the base class.
# It's important to note that when you override a method, the new implementation must have the same method signature as the original method. This means that the number and type of arguments, as well as the return type, must be the same.


# Another way to customize the behavior of a class is to call the base class method from the derived class method. To do this, you can use the super function. The super function allows you to call the base class method from the derived class method, 
# and can be useful when you want to extend the behavior of the base class method, rather than replace it.


from math import pi
class MathArea:
    def __init__(self,length,breadth):
        self.length=length        
        self.breadth=breadth

    def rectangleArea(self):
        return self.breadth*self.length   
        
class circle(MathArea):
    def __init__(self,radius):
        super().__init__(radius,radius)
        self.radius=radius

    def rectangleArea(self):    
        return pi*super().rectangleArea()
    
obj=MathArea(9.75,6.342)
print(obj.rectangleArea())  
cir=circle(5.31)
print(cir.rectangleArea())

