
value=int(input("Ente a number for multiplication table:"))
for i in range(11):
   if(i==10):
      break # it means that to exit the loop instade of exit the iteration that continue does that
   print(value ,"X ",i+1,"=",value*(i+1))