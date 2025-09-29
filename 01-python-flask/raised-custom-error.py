# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#     raise ValueError("Not a valid salary")


try:
    num=(input("Enter the integer orelse Quit:"))
    print(f"You entered {num}.")
except:
    raise ValueError("invalid")
