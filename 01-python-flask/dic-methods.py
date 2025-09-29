info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
info.update({'eligible':False})
print(f"\nAfter Update : {info}\n")
# 2nd one
# info.clear() #clears the entire dictionary
# print(info)
# # 3rd one
# info.pop('name')
# print(info)
# info.popitem() # removes the last item
# print(info)
# 4th one
del info['eligible'] # deletes the key value pair
print(info)