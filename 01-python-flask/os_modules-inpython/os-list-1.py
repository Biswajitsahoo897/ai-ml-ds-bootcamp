import os

print('currently working directory before was: ',os.getcwd())
os.chdir("/Users/biswa/onedrive")
# by this we can change the dirctory of an pyhton file or program
print('currently working directory after is: ',os.getcwd())
# os.chdir('../')


# creating a directory 
# import os
# print(os.name)
# os.mkdir()

os.rmdir("sample.txt") # it will remove the empty directory
os.remove("sample.txt") # it will remove the file