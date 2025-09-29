# this is the code for the variable length argument
value1=float(input("Enter the first  number :"))
value2=float(input("Enter the second  number :"))
def average(*number):
    print(type(number))
    sum=0
    for i in number:
        sum=sum+i
    print("Average is :",sum/len(number))
average(value1,value2)
def gm(a,b):
    c=(a*b)/(a+b)
    return c
print("The geometric mean is ",gm(value1,value2))