a = 69
# This is a type function
b = type(a) # class <int>

print(b)

#  similarlly 

a = "69"

b = type(a) # class <str>

print(b)

# Typecast

b = int(a)

print(b)

# if String is not convertable then it will show error

b = float(a)

print(b)