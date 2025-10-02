# *args 
def sum(*args):
    total=0
    print(type(args)) # <class 'tuple'>
    for i in args:
        total+=i
    return total

print(sum(432,34,123,67,8,4,2,99,29))

# **kwargs
def marks(**kwargs):
    print(type(kwargs)) # <class 'dict'>
    for key,value in kwargs.items():
        # print(item)
        # print(kwargs[item]) # print the values like 34,97,89
        print(f"{key} has scored {value} marks") 

marks(biswa=34,joe=97,sam=89,Dan=45)

# Note
# *args and **kwargs are special syntaxes in Python used in function definitions to handle variable numbers of arguments.
# *args ->allows a function to accept any number of positional arguments,
# **kwargs -> allows it to accept any number of keyword arguments.


# Combnining *args and **kwargs in a function

def func1(a,b,*args,**kwargs): # always *args should be before **kwargs
    print(a)
    print(b)
    print(args)
    print(kwargs)

func1(1,2,3,4,5,name="biswa",age=23,city="Bangalore")