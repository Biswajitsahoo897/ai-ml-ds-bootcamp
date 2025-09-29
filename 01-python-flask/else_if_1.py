# value=int(input("Enter the value :"))
# if(value<0):
#     print("The number is negative.")
# elif(value>0):
#     print("The number is positive.")
# else:
#     print(" Number is zero.")    

#more likly a number game ...hahahaha
value=int(input("Enter a number :"))
if(value<0):
    print("The number is negative.")
elif(value>0):
    print("The number is postive.........")
    if(value<=10):
        print("&The number is between 1-10")
    elif(value>10 and value<=20):
        print("& The number is between 11-20")       
    else:
        print("&The number is greater than 20....")     
else:
    print("You entered zero.")        