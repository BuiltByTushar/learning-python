li = (1, 2, 3, 4, 5)
print(type(li)) # It is a tuple

# For a single element 
a = (1,)
print(type(a))

b = () # It is a empty tuple

pie = (3, 1, 4, 1, 5)
print(pie.count(1))
print(pie.index(1))

concatenated = li + pie
print(concatenated)

print(li*3)

print(1 in pie) #Bolean : TRUE

print(len(li))

print(min(pie))

print(max(pie))

pie_approx = pie[:3]
print(pie_approx)

# Unpacking a tuple 
# Lets assign a unique individual variable to each element in tuple

A, B, C, D, E = pie
print(f"value of pie :  {A}.{B}{C}{D}{E}")