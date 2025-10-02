numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())

# Example 
while (data:=input("Enter the Value:")):
    print(data)
    if(data=="q" or data=="Q"):
        break