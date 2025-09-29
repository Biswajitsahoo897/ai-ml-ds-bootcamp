# # Static methods in Python are methods that belong to a class rather
# # than an instance of the class. They are defined using the
# # @staticmethod decorator and do not have access to the instance of
# # the class (i.e. self). They are called on the class itself, not on an
# # instance of the class. Static methods are often used to create utility
# # functions that don't need access to instance data.

# class math:
#     def __init__(self,num):
#         self.num=num
#     def addtornum(self,n):
#         self.num=self.num +n
#     @staticmethod
#     def add(a,b):
#         return a+b 
# result=math.add(7.23,90)
# print(result)           
# h=math(7)
# print(h.num)
# # h.addtornum(78)
# # print(h.num)



class Math:
            
    @staticmethod
    def add(a, b):
        return a + b

result = Math.add(1, 2)
print(result)

class StringUtils:
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

# Using the static method
print(StringUtils.is_palindrome("malayalam"))  # Output: True
print(StringUtils.is_palindrome("madam"))  # Output: True
print(StringUtils.is_palindrome("hello"))  # Output: False

