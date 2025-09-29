# Decorater is a function that takes a function , it creates a new function inside its 
# body(wrapper). Then it returns the NEW function.
# 1 
def add_greetings(func):
    def wrapeer():
        print("Hello Sir!!")
        func()
        print("Goodbye Sir!!")
    return wrapeer
    
# Mehtod 1 to use the decorator
@add_greetings
def hello_user():
    print("hello world!!")        

# Method 2 
f=add_greetings(hello_user)
f()




# Example 2
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(name):
    print(f"Hello {name}")

say_hello("Biswajit")