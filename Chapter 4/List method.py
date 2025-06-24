Friend = ["Apple", "Oranges",5, 345.34, False, "Aakash", "Rohan" ]

print(Friend)

Friend.append("Tushar") # Adds it at the end of the list

print(Friend)

l1 = [2, 4, 1, 5, 3, 9, 33, 43, 11, 7]
l1.sort() # sort in accending order
print(l1)
# for decending order
l1.reverse()
print(l1)

# lets add lol at 4th place in the list
l1.insert(3 ,"lol")
print(l1)

# lets remove it now
print(l1.pop(3))
print(l1)

# lets delete a Friend
Friend.remove("Aakash")
print(Friend)
