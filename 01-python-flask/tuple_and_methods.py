tup=(1,3,2,2,3,4,5,"me and myself",True,"kunu",False,3.1415)   #tuple is immutable that is it can't be changed unlike list
print("Displaying the tuple.......\n",tup)
value=(input("enter a number to search in the tuple:  \t"))
if value in tup:
    print("Yes ," ,value, "is present in the tuple .")
else:
    print("No!!!!!!!,That is absent.")    
print(type(tup))