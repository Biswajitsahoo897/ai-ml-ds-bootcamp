from typing import Any

class employee:
    # Used for instantiation of the object (called by default when object is created)
    def __init__(self,name):
        self.name=name
    def __len__(self):
        i=0
        for _ in self.name:
            i+=1
        return i
    def __str__(self) -> str:
        return f"The name of the Employee is {self.name}"
    def __repr__(self) -> str:
        return f"employee {self.name}"
    def __call__(self) -> str:
        return f"Hey i am inside the call method"

obj=employee("Binaya")    
# print(obj.__str__()) 
print(obj.__len__()) 
print(str(obj)) # magic method __str__ is called here
print(repr(obj)) # magic method __repr__ is called here
print(obj.__call__())
