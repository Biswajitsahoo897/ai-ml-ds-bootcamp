# The union() and update() methods prints all items that are present in the two sets. 
# The union() method returns a new set whereas update() method adds item into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

# The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)



s1={1,3,"tom",2,"me",4,5}
s2={3,2,"tom",1,"youtube",89}
s1.intersection_update(s2)
print(s1)
# A symmetric B=AUB-A intersection B
print(s1.symmetric_difference(s2))
print(s1.symmetric_difference_update(s2))
print(s1.difference(s2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
cities3 = cities.difference_update(cities2)
print(cities3)

