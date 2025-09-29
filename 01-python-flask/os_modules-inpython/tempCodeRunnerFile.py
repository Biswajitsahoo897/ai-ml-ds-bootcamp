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
