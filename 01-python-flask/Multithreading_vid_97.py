# Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. 
# In Python, we can use the threading module to implement multithreading. 
# In this tutorial, we will take a closer look at the threading module and its various functions and how they can be used in Python.
### code of harry
# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

# # Indicates some task being done
# def func(seconds):
#   print(f"Sleeping for {seconds} seconds")
#   time.sleep(seconds)
#   return seconds

# def main():
#   time1 = time.perf_counter()
#   # Normal Code
#   # func(4) 
#   # func(2)
#   # func(1)
  
  
#   # Same code using Threads
#   t1 = threading.Thread(target=func, args=[4])
#   t2 = threading.Thread(target=func, args=[2])
#   t3 = threading.Thread(target=func, args=[1])
#   t1.start()
#   t2.start()
#   t3.start()
  
#   t1.join()
#   t2.join()
#   t3.join()
#   # Calculating Time 
#   time2 = time.perf_counter()
#   print(time2 - time1)


# def poolingDemo():
#   with ThreadPoolExecutor() as executor:
#     # future1 = executor.submit(func, 3)
#     # future2 = executor.submit(func, 2)
#     # future3 = executor.submit(func, 4)
#     # print(future1.result())
#     # print(future2.result())
#     # print(future3.result())
#     l = [3, 5, 1, 2]
#     results = executor.map(func, l)
#     for result in results:
#       print(result)
# poolingDemo()






import threading
import time
from concurrent.futures import ThreadPoolExecutor
# indicates some task being done 
def func(seconds):
    print(f"Sleeping for {seconds} seconds\n")
    time.sleep(seconds)
time1=time.perf_counter()
# normal wala code
# func(4)
# func(2)
# func(1)
# same code using threads
def main():
    t1=threading.Thread(target=func ,args=[4])
    t2=threading.Thread(target=func ,args=[2])
    t3=threading.Thread(target=func ,args=[1])

    t1.start()
    t2.start()
    t3.start()
    time2=time.perf_counter()
    print(f"Time required :{time2-time1}")


def poolingdemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # future = executor.submit(func,3)
        # future = executor.submit(func,1)
        # future = executor.submit(func,4)
        # print(future.result())
        # print(future.result())
        # print(future.result())
        # return
        l=[2,5,7,1]
        results=executor.map(func,l)
        for result in results:
            print(result)
poolingdemo()
