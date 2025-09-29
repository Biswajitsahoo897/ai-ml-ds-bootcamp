#let's take an example of this square funtion
def square(n):
    '''takes in a number n, returns the square of n'''
    print("The square of ", n,"is:",n**2)

n=float(input("Enter the a number :")) 
square(n) 
print(square.__doc__)
#THE BASIC DIFFERENCE BETWEEN THE COMMENTS AND THE DOC STRING IS ...IT IS WRITTE ABOVE OR DOWN THE FUNTION UNLIKE COMMENTS