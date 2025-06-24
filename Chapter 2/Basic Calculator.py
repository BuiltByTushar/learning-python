# Basic Calculator

print("Type '1' for Addition, '2' for Subtraction, '3' for Multiplication and '4' for Division ")

AO = input("1(+) or 2(-) or 3(*) or 4(/):        -> ")

# Now convert it into integer
AO = int(AO)

if (AO == 1):
   print("Addition of A + B")
   A = input("A :  ->")
   A = int(A)
   B = input("B :  ->")
   B = int(B)
   print(A+B)
elif (AO == 2):
   print("Subtraction of A - B")
   A = input("A :  ->")
   A = int(A)
   B = input("B :  ->")
   B = int(B)
   print(A-B)
elif (AO == 3):
   print("Multiplication of A * B")
   A = input("A :  ->")
   A = int(A)
   B = input("B :  ->")
   B = int(B)
   print(A*B)
elif (AO == 4):
   print("Division of A / B")
   A = input("A :  ->")
   A = int(A)
   B = input("B :  ->")
   B = int(B)
   if (B == 0):
      print("UNDEFINED")
   else: print("Here Your answer :  ", A/B)
else: print("Invalid input please Type '1' for Addition, '2' for Subtraction, '3' for Multiplication and '4' for Division")

    



