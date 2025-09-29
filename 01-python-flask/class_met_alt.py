# THIS IS THE PROGRAM OF THE CLASS METHODS AS AN ALTERNATIVE

# class employee:
#     def __init__(self,na,a,sa):
#         self.name=na
#         self.age=a
#         self.salary=sa   
#     @classmethod
#     def fromstring(cls,string):
#         return cls(string.split("~")[0],int(string.split("~")[1]),int(string.split("~")[2]))    
#     # in this cls is same as employee and we have to parse three argument , it is just an instance of the class 
# obj_1=employee("Ashish",19,89203)
# print(obj_1.name)
# print(obj_1.age)
# print(obj_1.salary)

# # in this way we can print all the parameter value inside the funtion itself

string="Conqueror~20~90120"
print(string.split("~")[0])
print(string.split("~")[1])
print(string.split("~")[2])

# string="Biswajit~23~60190"
# obj_2=employee.fromstring(string)
# print(obj_2.name)
# print(obj_2.age)
# print(obj_2.salary)


# # this prints all the name age, and salary

# print(string.split("~"))


# class person:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#         self.vesion=23
# p=person("Binaya",50)
# print(p.name,p.age)

# print(p.__dict__)
# print(help(person))
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split('-')
        return cls(name, int(age))
obj = Person.from_string("John Doe-39")
print(obj.name,obj.age)
obj_1=Person.from_string("Srikant-28")
print(obj_1.name,obj_1.age)

# class Rectangle:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height

#   @classmethod
#   def square(cls, size):
#     return cls(size, size)
# rectangle = Rectangle.square(10)
# print(rectangle.height,rectangle.width)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("John", 30)
print(p.__dict__)