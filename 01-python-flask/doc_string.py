#let's take an example of this square funtion
def square(n):
    '''takes in a number n, returns the square of n'''
    print("The square of ", n,"is:",n**2)

n=float(input("Enter the a number :")) 
square(n) 
print(square.__doc__)

#THE BASIC DIFFERENCE BETWEEN THE COMMENTS AND THE DOCSTRING IS
# ...IT IS WRITTEN ABOVE OR DOWN THE FUNCTION UNLIKE COMMENTS & IT IS ACCESSIBLE VIA THE __doc__ ATTRIBUTE
# ...WHICH IS A SPECIAL ATTRIBUTE THAT STORES THE DOCSTRING OF A FUNCTION, CLASS