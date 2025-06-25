set_1 = {1, 2 ,3 , 5, 7, 11}
print(set_1) 

set_1.add(13)
print(set_1)

print(len(set_1))
set_1.remove(11)
print(set_1)

set_2 = {1, 2, 3, 4, 5 ,6}

print(set_1.union(set_2))
# OR
print(set_1|set_2)

print(set_2.intersection(set_1))
# OR
print(set_2&set_1)

print(set_1.difference(set_2))
# OR
print(set_1-set_2)

to_remove = {2, 4, 6}
set_2 = set_2 - to_remove
print(set_2)

print(set_2.issubset(set_1))
# OR
print(set_1.issuperset(set_2))

set_2.clear()
print(set_1.isdisjoint(set_2))