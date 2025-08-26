i = 100
temp = 1
for i in range(100,1000):
    temp = i
    z = temp%10
    temp = temp//10 # FOR removing last digit use // 
    y = temp%10
    temp = temp//10
    x = temp%10
    temp = temp//10
    if (i == (x*x*x) + (y*y*y) + (z*z*z)):
        print(f"Armstrong number is {i}")
