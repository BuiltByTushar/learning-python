Name ="Tushar"
# remember a string is immutable means we can't change it
# For a slice we use name_of_the_variable[ : ]
y = Name[0:3] # Here charator 3 is NOT included
print(y)

y = Name[-4:-1]
print(y)

y = Name[:5] #mean it start at 0
print(y)
y = Name[1:] #mean it end at full lengh
print(y)

word = "Creativity"
y = word[1:9:2]
print(y)
