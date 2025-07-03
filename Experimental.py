factorial = int(input("Factorial of: "))
answer = 1

for x in range(0,factorial):
    answer = (factorial-x)*answer 
else: print(answer)

