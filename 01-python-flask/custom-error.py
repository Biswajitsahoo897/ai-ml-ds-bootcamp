# # Defining Custom Exceptions
# In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

# Here's the syntax to define custom exceptions:

# class CustomError(Exception):
#   # code ...
#   pass
# try:
#   # code ...
# except CustomError:
#   # code...
# This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.


salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

# p=int(input("Enter the integer: "))
# if (p<10 or p>20):
#     raise ValueError('value should be between 10 and 20')
