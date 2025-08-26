layer = int(input("how many layers:  "))
star = "*"
space = " "
y = 1
for x in range(1,layer*2,2):
    print(f"{space*(layer-y)}{star*x}{space*(layer-y)}")
    y += 1

side = int(input("Lengh of Square: "))

print("* "*side)

for x in range(1,side-1):
    print("*",end="")
    print("  "*(side-2),end="")
    print(" *")
else:
    print("* "*side)

table = int(input("Which table do you want: ---> "))
table_set = []

for x in range(1,11):
    table_set.append(table*x)
else:table_set.reverse()
print(table_set)

# OR

for x in range(1,11):
    print((11-x)*table)


n = int(input())
if (1<=n<=100):
    odd = set()
    even = set()
    for i in range(1,100,2):
        odd.add(i)
        even.add(i+1)
    print(odd)
    print(even)
    if (n in odd):
        print("Weird")
    if (n in even):
        if (2<=n<=5):
            print("Not Weird")
        if (6<=n<=20):
            print("Weird")
        else:
            print("Not Weird")        
                