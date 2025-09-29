f=open("hello.txt" , "r")
contents=f.read()
print(contents)

# READING THE FILE 
try:
    f=open('PYTHON\\hello.txt','r') 
    # print(f)  # Opens the file but doesn't guarantee it will be closed properly.
    contents=f.read()          # Reads the file contents into the variable 'contents'.
    print(contents)            # Prints the contents of the file.
    f.close()
except FileNotFoundError:
    print("The file hello.txt does not exist.")
except IOError:
    print("An error occurred while reading the file.")
except ValueError:
    print("Value error: An error occured while reading the value in the file ")    

# WRITTING THE FILE          

file=open('PYTHON\\hello.txt','w')
print(file)
file.write('hello,world !! i am something ')
file.close()

file=open('PYTHON\\hello.txt','r')
f=file.read()
print(f)

file.close()


# APPEENDING THE FILE

# file=open('PYTHON\\hello.txt','a')
# file.write("This text will be appended at the end of the txt file.")
# file=open('PYTHON\\hello.txt','r')
# f=file.read()
# print(f)
# # this will append every single time u run this code
# file.close()



# or
with open('PYTHON\\hello.txt','a') as f:
    f.write(" hey!! i am inside with ")


