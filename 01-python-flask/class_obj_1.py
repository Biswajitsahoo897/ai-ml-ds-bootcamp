class person:
    name="Biswajit"
    occupation='Web Developer'
    def info(self):
        print(f"{self.name} is a {self.occupation}.")
a =person() # creating an object of the class person
b=person()
# a.name= "lorem"
b.name= "lorem"
b.occupation="site manager"
# it changed thre name biswajit -> lorem 
print(a.name)   
a.info()   
b.info()  
# there self refers to the instance calling the method