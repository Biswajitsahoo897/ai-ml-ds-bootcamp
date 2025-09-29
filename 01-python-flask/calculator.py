# #this is the code for the calculator
# # a=34
# # b=23
# c=input("Enter the first number :")
# d=input("Enter the second number :")
# # g=input(int(c)+int(d))
# print("the addition of",c,"&",d, "is :",int(c)+int(d))
# print("the multiplication of",c,"&",d, "is :",int(c)*int(d))
# print("the division of",c,"&",d, "is :",int(c)/int(d))
# print("the substractionof",c,"&",d, "is :",int(c)-int(d))
# # print("The operations are respectively:- \n")
# print("the addition of",a,"&",b, "is :",a+b)
# print("the multiplcation of ",a,"&",b,"is :",a*b)
# print("the division of ",a,"&",b,"is :",a/b)
# print("the modulo of ",a,"&",b,"is :",a%b)
# print("the floating point value  of ",a,"&",b,"is :",a//b)
# print("the substraction of ",a,"&",b,"is :",a-b)


class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        

obj1 = MyClass()
# obj2 = MyClass()

obj1.print_class_variable() # Output: 2
# obj2.print_class_variable() # Output: 2