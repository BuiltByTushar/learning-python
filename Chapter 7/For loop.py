list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in list :
    print(x)

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for x in tuple :
    print(x)


# Here Set can also be printed
set = {1, 2, 3 ,4, 5, 6, 7, 8, 9, 10}

for x in set:
    print(x)

### If we want to make a list from set 

list_set = []
for x in set:
    list_set.append(x)

print(list_set)
print(type(list_set))  # It is a list


x = "*"

for x in range(1,6,2):  # Range(start,end,skip_value)
    print(x*"*")

# Itteration
name = "Tushar"

for x in name:
    print(x)
else:
    print("Done")

for x in range(80):
    print(x)
    if x == 3:
        break
else:
    print("complete")   # here due to break operator for statement never exausted

for x in range(4):
    print(f"Printing {x}")
    if x == 2:
        continue      # It skip print(x) iteration for x = 2
    print(x)

