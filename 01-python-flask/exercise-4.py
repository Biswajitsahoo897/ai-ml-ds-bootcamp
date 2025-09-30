# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode



print("Enter 0 for code or 1 for decode ")
value =int(input('Enter your choice:'))

def first_code():
    # print("there is nothing new")
    print( "this is the only code")


def second_decode():
     print('ofifoo')
match value:
    case 0:
        print('You entered the number  0 ')
        first_code()
    case 1:
        print('You entered the number  1')
        second_decode()
    case _:
        print("Invalid choice!!")
   