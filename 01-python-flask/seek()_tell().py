# seek() funtion allows you to move the current position within a file t oa specific point.
# The position is specified  in bytes and you can move either forward or backward from the current position 
with open('PYTHON\\seekfile.txt','r') as f:
    print('The type of f is: ',type(f))
    # move to the 10th byte in the file 
    f.seek(10)
    # read the next 5 bytes
    data=f.read(5)
    print(data)

    print('this is where u ended your reading at:',f.tell(),"Bytes")
    print(f.tell(),"Bytes")
    f.close()
    # tell() funtion returns the current position within the file,in bytes.
    # this can be useful for tracking the location within the file or seeking  to a specific position relative to the 
    # current position 

# with open('PYTHON\\seekfile.txt','w') as f:
#     f.write("hello world!!! i am a very good boy.")
#     f.truncate(12)
#     f.close()
#     # f.truncate(10)
# with open('PYTHON\\seekfile.txt','r') as f:
#     print(f.read())
#     f.close()