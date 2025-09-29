# # all the variable and methods (member funtion) in python ar ey defalut set to public.
# class employee:
#     def __init__(self) -> None:
#         self.__name='Conqueror'
#         # this is the private access modifier
# a=employee()
# # print(a.name)
# print(a._employee__name)
# print(a.__dir__())
# # print()
# # name mangling



class Student: 
    def __init__(self, age, name): 
        self._age = age  
        self.__name=name    # An indication of private variable
        
        def _funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
print(obj._age)
obj._funName()

# calling by object  of class Subject
# print(obj1._age)
# print(obj1._funName())



# # THIS IS THE EXAMPLE OF THE PROTECTED ACCESS MODIFIER
# class student:
#     def __init__(self) -> None:
#         self._name="the_conqueror"

#     def _funname(self):
#         return "anyname"
#     # is the protected method of the 
    
# class subject(student):
#     pass
# # subject of the inherited class
# obj_1=student()
# obj_2=subject()
# # THIS IS CALLING BY SUBJECT OF STUDENT CLASS
# print(obj_1._name)
# print(obj_1._funname)
# #THIS IS  CALLING OF OBJECT OF SUBJECT CLASS 
# print(obj_2._name)
# print(obj_2._funname)