import os
folder=os.listdir("data_folder")
print(folder)

for i in folder:
    print(os.listdir(f"data_folder/{i}"))


print('currently working directory before was: ',os.getcwd())
os.chdir("/Users/biswa/onedrive")
# by this we can change the dirctory of an pyhton file or program
print('currently working directory after is: ',os.getcwd())
# os.chdir('../')


# creating a directory 
# import os
# print(os.name)
# os.mkdir()