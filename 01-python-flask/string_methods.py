# name=input("enter the name :-")
# age=int(input("Enter the age:-")) 
# if name == 'Alice':
#     print('Hi, Alice.')
#  elif age < 12:
#     print('You are not Alice, kiddo.')
#  elif age > 100:
#     print('You are not Alice, grannie.')
#  elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')
t="hello my name is biswajit sahoo!!!!!"
print(len(t))
print(t.capitalize())
print(t.replace("my",",MY 90237"))
print(t.split())
print(t.rstrip())
print(t.count("!"))
str1="heisagoodboy"
print(str1.find("is"))
print(str1.isalnum())



text="hello!! , Python is a good programming language"
print(text.index("Python"))
print(text.lower())
print(text.upper()) 

# Padding and aligning strings
print(f"{text:>50}") # right align
print(f"{text:<50}") # left align
print(f"{text:^50}") # center align
# The meaning of 50 is the total width of the string including the original string
#  and the padding spaces

# character encoding and decoding
print(ord('a')) # 97
print(ord('A')) # 65
print(chr(98)) # b

pi=3.141592653589793
print(f"the value of pi is approximately {pi:.4f}")