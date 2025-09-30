# CONSTRUCTOR IN PYTHON 

# A constructor is a special method in a class used to create and initialize
# an object of a class. There are different types of constructors.
# Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an
# object is created of a class. The main purpose of a constructor is to
# initialize or assign values to the data members of that class. It cannot
# return any value other than None.


class person:
    # print()
    def __init__(self, n , o):
        # init is one of the reserved funtion in the oop and this is known as a constructor
        print("hey i am inside the constructor.")
        self.name=n
        self.occ=o
    def details(self):
        print(f"{self.name} is a {self.occ}.")
a =person("dilip","Developer")
b=person("bikash", "HR")
c=person("Binaya", "senior executive")
a.details()
b.details()  
c.details()      




# Default Constructor in Python

# When the constructor doesn't accept any arguments from the object and has
# only one argument, self, in the constructor, it is known as a Default
# constructor.

class Details:
    def __init__(self):
        print("animal Crab belongs to Crustaceans group")

obj1=Details()


