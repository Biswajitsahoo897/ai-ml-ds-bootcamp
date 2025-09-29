# there are different methods available in the os module for  creating a directory .
# os.mkdir()
# os.makedirs()


# import os
# dire="new_directory"
# parent_dir="E:/OtherS(E)"
# path_offile=os.path.join(parent_dir,dire)
# os.mkdir(path_offile)
# print(f"diretory {dire} is created which is inside the {parent_dir}.")



# by this we can make directory inside any folder.
# import os
# f=open('E:/OtherS(E)/new_directory','r')
# file=f.read()
# print(file)
# f.close()

# with open('E:/OtherS(E)/new_directory','w') as f:
#     f.write("hello world !! My name is biswajit sahoo and currently i am working at cisco")




# # Listing out Files and Directories with Python
# path="/"
# # dir_list=os.listdir(path)
# dir_list=os.listdir('E:/')
# print(f"Files and directories in E:{path} are : ")
# print(dir_list)

# Deleting Directory or Files using Python
# OS module provides different methods for removing directories and files in Python. These are – 

# Using os.remove()
# Using os.rmdir()

# I DELETED THE FIRST FILE I CREATED

# import os
# file="file_1.txt"
# location="E:/OtherS(E)/new_directory"
# path_offile=os.path.join(location , file )
# os.remove(path_offile)

# THIA THE SECOND FILE I AM DELETING 

# import os
# path_ofsec=os.path.join("E:/OtherS(E)/new_directory","file_2.txt")
# os.remove(path_ofsec)

# It uses the os.rmdir function to delete the directory.
#  If the directory is empty, it will be removed. If it contains files or subdirectories, you may encounter an error.

# USING OF rmdir()
try:
    import os 
    dire="new_directory"
    location="E:/OtherS(E)/"
    path_of_folder=os.path.join(location,dire)
    os.rmdir(path_of_folder)
except OSError:
    print("some error ocuured!!,perhaps directory may not exists")

# import os
# print(os.name)
# # it gives different  output on different interpreters 


# import os
# try:
#     filename = 'GFG.txt'
#     f = open(filename, 'r')
#     text = f.read()
#     f.close()
# except IOError:
#   print('Problem reading: ' + filename)




# os.popen() COMMAND

import os
fd = "my-file_1.txt"

f = open(fd, 'w')
f.write("Hello world!! , this is biswajit sahoo from india")
f.close()
f = open(fd, 'r')
text = f.read()
print(text)

f = os.popen(fd, 'w')
f.write("Hello")
f.close()



# # OS.RENAME( ) FUNTION
# import os
# file='hello.txt'
# os.rename(file, "hello_new_1.txt")

# # When we are working with os module always specify the
# #  absolute path depending upon the operating system the code can run on any os but
# #  we need to change the path exactly. If you try to remove a
# #  file that does not exist you will get FileNotFoundError. 



# import os
# file_exists=os.path.exists("PYTHON/hello_new_1.txt")
# print(file_exists)
import os



# import os #importing os module.
# os.remove("file_name.txt") #removing the file.

# 

# Using os.path.getsize() Function
# import os
# file=os.path.getsize("PYTHON/hello_new_1.txt")
# print(f"size od the file is {file} bytes")


# import os
# directory = "Nikhil"
# parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"
# path = os.path.join(parent_dir, directory)
# os.makedirs(path)
# print("Directory '% s' created" % directory)
# directory = "c"
# parent_dir = "D:/Pycharm projects/GeeksforGeeks/a/b"
# mode = 0o666
# path = os.path.join(parent_dir, directory)
# os.makedirs(path, mode)
# print("Directory '% s' created" % directory)