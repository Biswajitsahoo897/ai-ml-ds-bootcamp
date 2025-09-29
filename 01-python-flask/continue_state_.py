
value=int(input("Ente a number for multiplication table:"))
for i in range(11):
    if(i==9):
       print("Skip the iteration")
       continue
    print(value ,"X ",i+1,"=",value*(i+1))