# Getters

# Getters in Python are methods that are used to access the values of an object's
# properties. They are used to return the value of a specific property, and are
# typically defined using the @property decorator. Here is an example of a simple
# class with a getter method:

# class MyClass:
# def _init_(self, value):
# self ._ value = value

# eproperty
# def value(self):
# return self ._ value

# In this example, the MyClass class has a single property,_value, which is initialized
# in the init method. The value method is defined as a getter using the @property
# decorator, and is used to return the value of the_value property.

# To use the getter, we can create an instance of the MyClass class, and then access
# the value property as if it were an attribute:



# SETTERS IN PYTHON

# It is important to note that the getters do not take any
# parameters and we cannot set the value through getter
# method.For that we need setter method which can be added by
# decorating method with @property_name.setter
# Here is an example of a class with both getter 
# and setter:

class myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"value is {self._value}")


    @property
    def ten_value(self):
        return 10*self._value    
    # this is the getter 

    @ten_value.setter
    def ten_value(self , new_value):
        self._value=new_value/10
    #this is the setter 
    # just remember it that's it
obj_1var=myclass(10)
obj_1var.ten_value=34
print(obj_1var.ten_value)
obj_1var.show()        
# print(obj_1var.show)        