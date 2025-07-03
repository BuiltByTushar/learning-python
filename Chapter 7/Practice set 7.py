# 1. Write a program to print multiplication table of a given number using for loop.

for x in range(1,20,2):
    print(x+1)

# Write a program to greet all the person names stored in a list ‘l’ and which starts with S

l = ["Tushar", "Harry", "Shristi", "Sonu"]

for x in l:
    if "S" in x:
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

# 4. Write a program to find whether a given number is prime or not.

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
* * *
*   *   for n = 3
* * * 
'''

