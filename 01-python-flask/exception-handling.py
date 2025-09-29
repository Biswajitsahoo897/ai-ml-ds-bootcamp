# try:
#     y=input('Enter the number:')
#     print(f"here is the Multiplication table of {y}:")
#     for i in range(1,11):
#         print(f"{int(y)} X {int(i)}={int(y)*i} ")
# except:
#     print('Invalid input!!!')        


try:
    num =int(input('Enter an integer(0-5):'))
    f=[2,8,9,12,34,"me"]
    print(f[num])
except ValueError:
    print("number is not an integer")
except IndexError:
    print("Index error!!!")