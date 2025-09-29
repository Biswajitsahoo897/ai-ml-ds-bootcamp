class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        pass
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed                  
        
    def make_sound(self):
        print("Bark!")
        pass
print('this is the animal class')
var=Animal("Tiger","Tigress")
print(var.name,var.species)
print(var.make_sound())
print('this is the mammal class')
var1=Mammal("Elephant","ele_unknown")
print(var1.name)
print(var1.fur_color)

# The mro() method in Python stands for Method Resolution Order. 
# It is used to determine the order in which base classes are searched when executing a method. 
# This is particularly relevant in the context of multiple inheritance.
print(Dog.mro())




