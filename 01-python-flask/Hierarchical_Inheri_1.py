# Hierarchical Inheritance is a type of inheritance in Object-Oriented Programming where multiple subclasses inherit from a single base class. 
# In other words, a single base class acts as a parent class for multiple subclasses.
#  This is a way of establishing relationships between classes in a hierarchical manner.

# https://files.codingninjas.in/article_images/custom-upload-1671564863.webp

class animal:
    def __init__(self,n,year) -> None:
        self.name=n
        self.year=year
    def show_detailed(self):
        print(f"Name:-{self.name}")
        print(f"year:-{self.year}")

class dog(animal):
    def __init__(self, n, year, breed) -> None:
        super().__init__(n, year)
        self.breed=breed
    def show_detailed(self):
        print(f"Species: Dog")
        print(f"breed:-{self.breed}")
        return super().show_detailed()

class cat(animal):
    def __init__(self, n, year,color) -> None:
        self.color=color
        super().__init__(n, year)
        print(f"Species:cat")
        print(f"color:{self.color}")
        # return animal.show_detailed(self)

obj_1=dog("tommy",10,"Golden Retriever")
obj_1.show_detailed()
print("\n")
obj_2=cat("semie",6,"brown")
obj_2.show_detailed()