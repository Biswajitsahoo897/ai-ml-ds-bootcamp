while True:
    try:
        a=int(input("Enter a number : "))
        b=int(input("Enter another number: "))
        print(f"The division of {a} and {b} is {a/b}")

    except ZeroDivisionError:
        print("hey don't divide by zero")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"Unknown error occurred: {e}")


# Custom Exception

a=int(input("Enter a number : "))
b=int(input("Enter another number: "))
print(f"The division of {a} and {b} is {a/b}")
if b==0:
    raise ZeroDivisionError("b should not be zero")