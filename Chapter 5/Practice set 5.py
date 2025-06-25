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

while len(numbers) <= 8:
    numbers.add(input("Enter number here:-->"))

print(numbers)

# Can we have a set with 18 (int) and '18' (str) as a value in it?
