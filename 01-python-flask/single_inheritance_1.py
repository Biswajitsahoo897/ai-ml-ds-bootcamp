class animal:
    def __init__(self,name,species,id):
        self.name=name 
        self.species=species
        self.id=id
    def make_sound(self):    
        print("Sound made by this particullar animal")

class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name,species="dog1",id=903225) 
        self.name=name
        self.breed=breed 
        
    def make_sound(self):
        print("bark!!")
    

obj=animal("Gargi","cat",6294602)
print(obj.name,obj.species,obj.id)
print(obj.make_sound())

print("This is dog class  ")
var=dog("tommyy","labradog") 
print(var.name,var.id)
print(var.make_sound) 

# # print(obj1.make_sound())       
# # print(obj1.breed)       
