def cube(a):
    return a*a*a
list_1=[1,4,2,8,9,12,3.45,20]
new_list_1=[]
# for item_list in list_1:
#     new_list_1.append(cube(item_list))

new_list_1=list(map(cube,list_1))
# map(funtion,iterable)
print(new_list_1)
print(list_1)



def filter_funtion(a):
     return a>10
def filter_funtion_1(a):
     return a>5
newnewl=list(filter(filter_funtion,list_1))
print(newnewl)

newnewl2=list(filter(filter_funtion_1,list_1))
print(newnewl2)

# filter(predicate, iterable)
# the predicate argument is a funtion that returns a boolean value and is applied to the each elements in the iterable 
# argument can be list , tuple or any othe riterable object.


num=[1,3,5,12,10]
evens=filter(lambda x: x%2==0 , num)
print(list(evens))

