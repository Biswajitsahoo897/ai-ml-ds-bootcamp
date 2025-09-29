from typing import Any


class employee:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i
    def __str__(self) -> str:
        return f"The name of the Employee is ({self.name})"
    def __repr__(self) -> str:
        return f"employee ({self.name})"
    def __call__(self) -> str:
        print("Hey i am inside the call method")
obj=employee("Binaya")    
# print(obj.__str__()) 
print(obj.__len__()) 
print(str(obj))
print(obj.__call__)
print()