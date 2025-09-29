# class human:
#     def __init__(self, n, a) -> None:
#         self.name = n
#         self.age = a

#     def showdetailed(self):  # Corrected the typo from 'showdeatiled' to 'showdetailed'
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")


# class person(human):
#     def __init__(self, n, a, address) -> None:
#         super().__init__(n, a)
#         self.address = address

#     def showdetailed(self):  # Corrected the typo
#         print("This is working")
#         print(f"Address: {self.address}")
#         return super().showdetailed()


# class program:
#     def __init__(self, program_name, duration):
#         self.program_name = program_name
#         self.duration = duration

#     def showdetailed(self):  # Corrected the typo
#         print(f"Program Name: {self.program_name}")
#         print(f"Duration: {self.duration}")


# class student(person):
#     def __init__(self, n, a, address, program) -> None:
#         super().__init__(n, a, address)
#         self.program = program

#     def showdetailed(self):  # Corrected the typo
#         super().showdetailed()
#         self.program.showdetailed()  # Call the showdetailed method of the Program class


# # Create an object of the `Program` class
# pro = program("CSE", "4 YEARS")

# # Create an object of the `Student` class and pass the `pro` object
# std = student("Biswajit", 23, "BBSR Plot_no=6712", pro)

# # Call the `showdetailed` method to display all the details
# std.showdetailed()





class human:
    def __init__(self,n,a) -> None:
        self.name=n
        self.age=a
    def showdetailed(self):
        print(f"Name:-{self.name}")
        print(f"Age:-{self.age}")


class person(human):
    def __init__(self, n, a,address) -> None:
        super().__init__(n, a)
        self.address=address
    def showdetailed(self):
        print("This is working")
        print(f"Address:{self.address}")
        return super().showdetailed()
    # in this case return statement is not necessary u may remove it , u'll get the same output
class program:
    def __init__(self,program_name,duration):
        self.program_name=program_name
        self.duration=duration
    def showdetailed(self):
        print(f"program_name:{self.program_name}")
        print(f"Duration:-{self.duration}")

class student(person,program):
    def __init__(self, n, a, address,program) -> None:
        super().__init__(n, a, address)
        self.program=program
    def showdetailed(self):
        self.program.showdetailed()
        super().showdetailed() 

# obj_1=human("Biswajit",23)
# per=person("Biswajit",23,"Plot_no=6712")
# obj_1.showdetailed()
pro=program("CSE","4 YEARS")
std=student("Biswajit",23," BBSR Plot_no=6712",pro)
# std=student("Biswajit",23)
# per.showdetailed()
std.showdetailed()