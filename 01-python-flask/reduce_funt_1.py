from functools import reduce

# list of the number
num=[3,1,4,8,5]

avg=reduce(lambda x,y:(x+y)/2 , num)

print(avg)