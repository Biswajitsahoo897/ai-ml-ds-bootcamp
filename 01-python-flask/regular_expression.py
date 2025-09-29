# # Regular Expressions in Python
# # Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

# # Metacharacters in regular expressions
# # []  Represent a character class
# # ^   Matches the beginning
# # $   Matches the end
# # .   Matches any character except newline
# # ?   Matches zero or one occurrence.
# # |   Means OR (Matches with any of the characters
# #     separated by it.
# # *   Any number of occurrences (including 0 occurrences)
# # +   One or more occurrences
# # {}  Indicate number of occurrences of a preceding RE 
# #     to match.
# # ()  Enclose a group of REs

# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# # print(y.values())
# # print(y.keys())
# # print(y.items())
# print(y["age"])
# print(y["name"])
# print(x)


import re
text= "The Rain in spain, it is a very beautiful and the people there are very nice"
search=re.search("^The.*spain$",text)
search=re.search("is................",text)
search=re.search("is+",text)
print(search)
x=re.findall("beautiful..........",text)
print(x)

# import re
pattern = r"[A-Z]+at"
text = "The Cat is in the Hat."
# The findall() function returns a list containing all matches.
matches = re.findall(pattern, text)
print(matches)
x=re.search("\s",text)
print("The first white-space character is located in position :",x.start())
#The split() function returns a list where the string has been split at each match:
y=re.split("\s",text)
print(y)