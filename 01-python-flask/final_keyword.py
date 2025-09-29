def funtion1():
 try:
    l=[2,6,4,9]
    inp=int(input('Enter the index: '))
    print(l[inp])
    return 1
 except:
    print('some error ocurred')
    return 0
#  finally:
    # whatever u will write inside the final keyword it will executed    
#    print("i am always execute")
    print("i am always execute")
# x=
print(funtion1()) 
 


try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")
