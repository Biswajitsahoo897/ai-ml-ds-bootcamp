value=int(input("Enter the value of X:"))
match value:
    case 0:
        print("X is zero.")
    case 4:
        print("X is 4")
    case _ if value!=20:
        print(value," is not 20.")
    case _ if value!=30:
        print(value," is not 30.")
    case _ :
        print(value, " didn't satisfy any of your conditions")                

