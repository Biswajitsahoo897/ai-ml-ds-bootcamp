# The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized).
# The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time# 


# 1
import time
# Define the functions
def usingwhile():
    i = 0
    while i < 10000:
        i = i + 1
        print(i)
def usingfor():
    for i in range(10000):
        print(i)
# Measure time for the for loop
start_time = time.time()
usingfor()
time_taken_for = time.time() - start_time
start_time = time.time()
usingwhile()
time_taken_while = time.time() - start_time
print(f"Time taken to complete the for loop is : {time_taken_for:.5f} sec")
print(f"Time taken to complete the while loop is : {time_taken_while:.5f} sec")


# 2
# import time
# print("Start:", time.time())
# time.sleep(4)
# print("End:", time.time())

# 3
import time
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)
