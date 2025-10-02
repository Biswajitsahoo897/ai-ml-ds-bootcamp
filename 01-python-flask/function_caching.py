# funtion caching is a technique for improving the performance of a program by storing the results of funtion call so that you can reuse 
# the results instead of recomputing then every single time the function is called.


import functools
import time
@functools.lru_cache(maxsize=None,typed=True)
def function_cache(x):
    time.sleep(2)
    return 2*x
print(function_cache(12))
print("done for 12")
print(function_cache(20))
print("done for 20")
print(function_cache(35))
print("done for 35")

# again called the same function for the fetching the data from the cache 
print(function_cache(12))
print("done for 12")
print(function_cache(20))
print("done for 20")
print(function_cache(35))
print("done for 35")

# def fibo(x):
#     if(x<2):
#         return x
#     return fibo(x-1)+fibo(x-2)
# # this will print the 10th value 
# print(fibo(20))
# print(fibo(10))
# print(fibo(6))
# print(fibo(9))
# time.sleep(5)
# print(fibo(9))
# print(fibo(6))
# print(fibo(10))
# print(fibo(20))
# # 6765