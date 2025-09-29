# class exclass:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     def info(self):
#         print("This is an example")
# obj1=exclass("Maharshi",56)
# print(obj1._name)
# print(obj1._age)







class Student: 
    def __init__(self, age, name): 
        self.__age = age      # Private variable
        self.name = name      # Public variable

    def __funName(self):      # Private function
        self.y = 34
        print(self.y)

    def access_private_method(self):  # Public method to access private function
        self.__funName()

    def get_age(self):        # Public method to access private variable
        return self.__age

class Subject(Student):
    pass

obj = Student(21, "Harry")
obj1 = Subject(22, "Ron")

# Accessing private attribute through a public method
print(obj.get_age())

# Accessing private method through a public method
obj.access_private_method()

# Accessing private attribute and method in the Subject class
print(obj1.get_age())
obj1.access_private_method()

# Incorrect direct access of private attributes (will raise AttributeError)
# print(obj.__age)
# print(obj.__funName())

# Incorrect direct access of private attributes in inherited class (will raise AttributeError)
# print(obj1.__age)
# print(obj1.__funName())
        
#NAME MANGLEING IN PYTHON (PRIVATE)
# 
# 
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute        