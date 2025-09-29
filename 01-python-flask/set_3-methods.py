cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

set1={
    "me",34,2,5,90,"here","delhi"
}
set2={
    1,2,3,34,90,"united states","india"
}
print(set1.isdisjoint(set2))


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

print("checking for the number..")
number1={1,0,2,12,3,4,90,45}
number2={2,1,90}
print(number1.issuperset(number2))
print(number1.issubset(number2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

cities.remove("Tokyo")
print(cities)

item = cities.pop()
print(cities)
print(item)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")