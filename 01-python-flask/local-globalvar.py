a=3
print(f"The value global a : {a}")

def local_fun():
    global a
    # this will change the value of the global variable a
    a=8
    print(f"the value local a is {a}")
    u="you are just crazy"
# a local variable is a variable that defines within the funtion and is only accessable within that funtion.It is created when 
# the funtion is called and it is destroyed when the funtion is returned

# on the other hand a global variable , can be accessable anywhere however it won't destroyed by any funtion.
local_fun()
print("The new value of global is  ",a)
# print(u) you can't do this