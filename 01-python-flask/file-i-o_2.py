# f=open('PYTHON\\myfile.txt','r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)
# read_file=f.read()
# print(read_file)


# f=open('PYTHON\\myfile.txt','r')
# i=0
# while True:
#     line=f.readline()
#     i=i+1
#     if not line:
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"Marks of the student {i} in maths is : {m1}")
#     print(f"Marks of the student {i} in physics is : {m2}")
#     print(f"Marks of the student {i} in chemistry is : {m3}")
    
#     print(line)
    




# USING OF READLINE() and split() funtion in python

# with open("PYTHON\\hello_new_1.txt",'r') as file:
#     data=file.readline(6)
#     for line in data:
#         word =line.split()
#         print(word)

with open("PYTHON\\myfile.txt" ,'w') as f:
    f.write("hello World!!!")
    f.close()

with open("PYTHON\\myfile.txt" ,'r') as f:
    file_read=f.read()
    print(file_read)


