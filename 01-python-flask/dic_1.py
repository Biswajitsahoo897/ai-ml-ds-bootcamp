info={"name":'conqueror','age':19, 'college':'CGU', 'ELIGIBLE':True}
print(info['name'])
print(info["name"])
print(info.get('name'))
# they are exactly the same but ..IF there's no key with name then it returns none but the upper one throws an error occuired

# info = {'name':'Karan', 'age':19, 'eligible':True}
dic={
    344:"biswajit",
    144:"dilip",
    190:"ashish",
    424:'meena'
}
print(dic) 
print(dic[190])
print(dic[144])
# print('this prints the keys in the info parts')
for key in info.keys():
    print(f"the value corresponding to the key {key} is {info[key]}")

print(info.items())