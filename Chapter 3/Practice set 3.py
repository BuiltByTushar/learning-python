# Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Please enter your name here:\u2192")

import time
current_hour = time.localtime().tm_hour

if (current_hour < 5):
    print("Good Night \U0001F319", name)
elif (current_hour < 11):
    print("Good Morning \u2600", name)
elif (current_hour < 17):
    print("Good Afternoon \U0001F324", name)
elif (current_hour < 20):
    print("Good Evening \U0001F307", name)
else: print("Good Night \U0001F319", name)

# Write a program to fill in a letter template given below with name and date.
applicant = input("Please enter your Name:\u2192")
date = input("Type Today's Date (dd/mm/yy):")
# Now I am going to convert mm into individual months

month_code = int(date[3:5])
if ( month_code == 12 ):
    month = "January"
elif ( month_code == 1 ):
    month = "February"
elif ( month_code == 2 ):
    month = "March"
elif ( month_code == 3 ):
    month = "April"
elif ( month_code == 4 ):
    month = "May"
elif ( month_code == 5 ):
    month = "June"
elif ( month_code == 6 ):
    month = "July"   
elif ( month_code == 7 ):
    month = "August"
elif ( month_code == 8 ):
    month = "September"
elif ( month_code == 9 ):
    month = "October"   
elif ( month_code == 10 ):
    month = "November"
elif ( month_code == 11 ):
    month = "December"
else: print("INVALID")    

import random

if month_code == 12 or 2 or 4 or 6 or 8 or 10:
    appointment_date = random.randint(1,31)
elif month_code == 3 or 5 or 7 or 9 or 11:
    appointment_date = random.randint(1,30)
else: appointment_date = random.randint(1,28)

print(f"Congratulations !\n{applicant.capitalize()} is selected \u2705 \nAppear at {appointment_date} of {month}")

# Write a program to detect double space in a string.
# Replace the double space from problem 3 with single spaces

string = "Tushar is  a good  boy"

if "  " in string:
    string = string.replace("  "," ")
    print("This sentence contains double space")
    print(f"Corrected sentence:\n{string}")
else: print("no error")


# Write a program to format the following letter using escape sequence characters.

letter = "Dear Harry, \n\tThis python course is nice. \nThanks!"
print(letter)