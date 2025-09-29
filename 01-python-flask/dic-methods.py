info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
# 2nd one
# info.clear()
# print(info)
# # 3rd one
# info.pop('name')
# print(info)
# info.popitem()
# print(info)
# 4th one
del info['eligible']
print(info)