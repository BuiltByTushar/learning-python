# 1. Write a program to print multiplication table of a given number using for loop.

for x in range(1,20,2):
    print(x+1)

# Write a program to greet all the person names stored in a list ‘l’ and which starts with S

l = ["Tushar", "Harry", "Shristi", "Sonu"]

for x in l:
    if x.startswith("S"):
        print(f"Hello {x}")
        continue
    else: print(f"Bye {x}")
    
# 3. Attempt problem 1 using while loop.

table = int(input("Which table do you want: ---> "))
x = 1
while x <= 10:
    print(table*x)
    x += 1
else:print("Complete")

#### 4. Write a program to find whether a given number is prime or not.

n = int(input("Type any natural number:  "))

if n <=  0:
    print("Try Again")
elif n == 1:
    print("1 is a unit and not a Prime number")
else:
    for x in range(2,n):
        if n%x == 0:
            print("Number is not Prime")
            break
        else: 
            print("Number is Prime")
            break

# 5. Write a program to find the sum of first n natural numbers using while loop.

n = int(input("sum up to: "))

print(((n*n) + n)/2)

# 6. Write a program to calculate the factorial of a given number using for loop.

factorial = int(input("Factorial of: "))
answer = 1

for x in range(0,factorial):
    answer = (factorial-x)*answer 
else: print(answer)


# Using WHILE LOOP

x = 0
while x < factorial:
    answer = (factorial-x)*answer 
    x+=1
else: print(answer)

'''
Write a program to print the following star pattern.
  *
 ***
*****
'''

layer = int(input("how many layers:  "))
star = "*"
space = " "
y = 1
for x in range(1,layer*2,2):
    print(f"{space*(layer-y)}{star*x}{space*(layer-y)}")
    y += 1


'''
Write a program to print the following star pattern.
* * *
*   *   for n = 3
* * * 
'''

for x in range(1,4):
    if x == 2:
        print("*   *")
        continue
    print("* * *")

# OR

side = int(input("Lengh of Square: "))

print("* "*side)

for x in range(1,side-1):
    print("*",end="")
    print("  "*(side-2),end="")
    print(" *")
else:
    print("* "*side)


# Write a program to print multiplication table of n using for loops in reversed order

table = int(input("Which table do you want: ---> "))
table_set = []

for x in range(1,11):
    table_set.append(table*x)
else:table_set.reverse()
print(table_set)

# OR

for x in range(1,11):
    print((11-x)*table)