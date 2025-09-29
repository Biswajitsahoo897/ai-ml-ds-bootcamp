# i1=int(input("Enter i: "))
# j1=int(input("Enter j:"))
# k1=int(input("Enter k:"))

# class pyth_vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
        
#     # def __add__(self,i1,j1,k1):
#     #     return pyth_vector(self.i+i1 , self.j+j1 , self.k+k1)
        
#     # def __add__(self,u):
#     #     return pyth_vector(self.i+u.i , self.j+u.j , self.k+u.k)#if u don't want user definied then do this instade
#     def __add__(self,u):
#         return pyth_vector(self.i+u.i , self.j+u.j , self.k+u.k)#if u don't want user definied then do this instade
    

# obj=pyth_vector(i1,j1,k1)
# # print(type(obj))
# vect=pyth_vector(2,4,5)

# print(obj)
# print(vect)
# print("---------------------  +")
# print(obj+vect)    
# # print(type(obj))
# # print(type(vect))
# # this define or shows the type which is vector itself only


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x={self.x} ,y={self.y}"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
var=Point(5,9)   
print(var)
var2=Point(7,1) 
print(var2)
print("---------+")
print(var+var2)



