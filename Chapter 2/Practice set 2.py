# Q. Write a python program to find remainder when a number is divided by z
print("Remainder finder:  input A/B")
A = int(input("A:  ->"))
B = int(input("B:  ->"))
if (B == 0):
    print("INVALID! B CAN NOT BE ZERO")
else: print(A % B)


# Q. Check the type of variable assigned using input () function
car = input("Type here")
print(type(car))

# Q. Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80
a = 34
b = 80
x = a > b
print(x)

# Q. Write a python program to find an average of two numbers entered by the user
print("Average of two number: ")
number_1 = input("Value 1:  ->")
number_2 = input("Value 2:  ->")
print((int(number_1)+int(number_2))/2)

# Q. Write a python program to calculate the square of a number entered by the user
print("Square of number")
y = int(input("Type number"))
print("Square here:  ->",y**2)

