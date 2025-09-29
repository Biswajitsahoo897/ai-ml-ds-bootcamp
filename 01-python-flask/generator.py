# def fibonacci(value):
#     a,b=0,1
#     while b < value:
#         yield b
#         a , b= b ,a+b
#         # print(f"{a}")
# # this will create a generator object
# a=fibonacci(1000)
# for i in a:#this will iterate through the genrator object
#     print(f"{i}")        

# Generators in Python
# Generators in Python are special type of functions that allow you to create an iterable sequence of values. 
# A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it. 
# Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.
def my_generator():
    for i in range(5000):
        yield i
# yield statement returns a value to the function 
gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))