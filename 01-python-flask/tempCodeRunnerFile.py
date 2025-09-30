a=int(input("Enter a number : "))
b=int(input("Enter another number: "))
print(f"The division of {a} and {b} is {a/b}")
if b==0:
    raise ZeroDivisionError("b should not be zero")