# Write a program to create a dictionary of Hindi words with values as their English translation.
# Provide user with an option to look it up!
dictionary = {"Namaste":"Hello",
              "Haan":"Yes",
              "Nahin":"No",
              "Dhanyavaad":"Thank you",
              "Kripya":"Please",
              "Maaf kijiye":"Sorry",
              "Theek hai":"Alright",
              "Accha":"Okay",
              "Bura":"Bad",
              "Sundar":"Beautiful",
              "Bada":"Big",
              "Chhota":"Small",
              "Jaldi":"Quickly",
              "Dheere":"Slowly",
              "Main":"Me",
              "Tum":"You",
              "Aap":"You",
              "Woh":"That",
              "Yeh":"This",
              "Hum":"We",
              "Kya":"What",
              "Kyon":"Why",
              "Kab":"When",
              "Kahan":"Where",
              "Kaise":"How",
              "Khaana":"Food/to eat",
              "Paani":"Water",
              "Chai":"Tea",
              "Namak":"Salt",
              "Cheeni":"Sugar",
              "Ghar":"Home",
              "Dawa":"Medicine",
              "Paisa":"Money",
              "Dukaan":"Shop",
              "Bazaar":"Market",
              "Kapda":"Cloth",
              "Kitaab":"Book",
              "Kalam":"Pen",
              "Baccha":"Child",
              "Aadmi":"MAn",
              "Aurat":"Women",
              "Naam":"Name",
              "Kaam":"Work",
              "Raasta":"Way/Road",
              "Madad":"Help"}

word = input("Hindi Word: -->")
word = word.capitalize()
print(dictionary.get(word))

if (input("type LIST for the Whole Dictionary: --->").upper() == "LIST"):
    print(dictionary.items())
else: 
    print("INVALID")

# Write a program to input eight numbers from the user and display all the unique numbers (once)

numbers = set()

while len(numbers) < 8:
    numbers.add(int(input("Enter number here:-->")))

print(numbers)

# Can we have a set with 18 (int) and '18' (str) as a value in it?

# YES

example = {18, "18"}
print(example)

# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))
# As 20 and 20.0 are same they are only given one value inside set

dic = {}
# What is the type of 's'?
print(type(dic))

# It is a empty dictionary

# Create an empty dictionary. 
# Allow 4 friends to enter their favorite language as value and use key as their names. 
# Assume that the names are unique.

dic = {}

L1 = input("Rahul Type your favorate language: --->")
L2 = input("Mohan Type your favorate language: --->")
L3 = input("Krish Type your favorate language: --->")
L4 = input("Raju Type your favorate language: --->")

dic.update({"Rahul":L1})
dic.update({"Mohan":L2})
dic.update({"Krish":L3})
dic.update({"Raju":L4})

print(dic.items())

# If the names of 2 friends are same; what will happen to the above program ?
# now take Mohan be Rahul
dic.pop("Mohan")
print(dic.items())

dic.update({"Rahul":L2})
print(dic.items())
# It UPDATES the value for that key

# If languages of two friends are same; what will happen to the above program ?
# They still have different key value pair

# Can you change the values inside a list which is contained in set S ?
# S = {8, 7, 12, "Harry", [1,2]}
# no as list are not hashable 
S = {8, 7, 12, "Harry, (1,2)"}
# We used tuple insted