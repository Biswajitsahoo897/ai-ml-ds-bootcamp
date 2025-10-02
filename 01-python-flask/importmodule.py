# import math

print(math.factorial(5))
print(math.pow(2.5,3))
print(math.sqrt(8.7221))
print("the value of sin 30  :",math.sin(30))



from math import sqrt , pi, pow
result=sqrt(9.23)*4.329*pi
print(result)


# this imports everythings
from math import *
print("the value of pi : ",pi)


# use of 'as' keyword in python
# import math as m
from math import pi, sqrt as s
value=s(4)*pi
print(value)

# use of dir funtion in the python
import math
print(dir(math))
print(math.nan, type(math.nan))


from theconq import welcome,var
from theconq import *
# from theconq import welcome as w
# we can also do this

welcome()
print(var)
