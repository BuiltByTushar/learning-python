# 1. Write a program to find the greatest of four numbers entered by the user.

print("Greatest number Finder")
numbers = set()

while len(numbers) < 4 :
    numbers.add(int(input("Type any number:--> ")))

print(f"Greatest of four numbers is {max(numbers)}")

# Write a program to find out whether a student has passed or failed 
# if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 5 subjects and take marks as an input from the user.

print("Student Result")
student_name = input("Name of the student:  ").capitalize()
physics_marks = int(input(f"Marks of {student_name} out of 100 in Physics: "))
chemistry_marks = int(input(f"Marks of {student_name} out of 100 in Chemistry: "))
maths_marks = int(input(f"Marks of {student_name} out of 100 in Maths: "))
english_marks = int(input(f"Marks of {student_name} out of 100 in English: "))
computer_marks = int(input(f"Marks of {student_name} out of 100 in Computer: "))

subject_index = 0

if (physics_marks < 33):
    print("FAILED IN PHYSICS")
elif (physics_marks == 100):
    print("Congratulations! for full score 'PASSED IN PHYSICS'")
    subject_index += 1
elif (physics_marks >= 33):
    print("PASSED IN PHYSICS")
    subject_index += 1
else: print("INVALID MARKS") 


if (chemistry_marks < 33):
    print("FAILED IN CHEMISTRY")
elif (chemistry_marks == 100):
    print("Congratulations! for full score 'PASSED IN CHEMISTRY'")
    subject_index += 1
elif (chemistry_marks >= 33):
    print("PASSED IN CHEMISTRY")
    subject_index += 1
else: print("INVALID MARKS")


if (maths_marks < 33):
    print("FAILED IN MATHS")
elif (maths_marks == 100):
    print("Congratulations! for full score 'PASSED IN MATHS'")
    subject_index += 1
elif (maths_marks >= 33):
    print("PASSED IN MATHS")
    subject_index += 1
else: print("INVALID MARKS")

if (english_marks < 33):
    print("FAILED IN ENGLISH")
elif (english_marks == 100):
    print("Congratulations! for full score 'PASSED IN ENGLISH'")
    subject_index += 1
elif (english_marks >= 33):
    print("PASSED IN ENGLISH")
    subject_index += 1
else: print("INVALID MARKS")


if (computer_marks < 33):
    print("FAILED IN COMPUTER")
elif (computer_marks == 100):
    print("Congratulations! for full score 'PASSED IN COMPUTER'")
    subject_index += 1
elif (computer_marks >= 33):
    print("PASSED IN COMPUTER")
    subject_index += 1
else: print("INVALID MARKS")

percentage = (physics_marks + chemistry_marks + maths_marks + english_marks + computer_marks)/5 
if (subject_index == 5 and percentage >= 40):
    print(f"{student_name} has PASSED")
elif (subject_index == 5 and percentage < 40):
    print(f"{student_name} has FAILED due to less than 40% overall")
else: print(f"{student_name} has FAILED")
print(f"{student_name} has scored {percentage}%")
# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
# Write a program to detect these spams.

print("Welcome to SCAM detection program")
inbox = input("Paste the message: ")
inbox = inbox.lower()
if (inbox == "make a lot of money" or "buy now" or "subscribe this" or "click this"):
    print("SPAM")
else : print("not likely SPAM")

# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Login Username here:--> ")
user_index = 0
while user_index < 1:
    if (len(username) >= 10): 
        print(f"Welecome {username}")
        user_index += 1
    elif len(username) < 10 :
        print("Invalid username please make it at least 10 characters")
        username = input("Try again: ")

# Write a program which finds out whether a given name is present in a list or not.

name_list = ["Tushar", "Aarav", "Arjun", "Aditya", "Vihaan", "Vivaan", "Krish", "Aryan", "Atharv", "Rohan", "Rahul",
"Siddharth", "Kabir", "Om", "Ansh", "Shaurya", "Yuvraj", "Dhruv", "Karthik", "Pranav", "Manav",
"Ayush", "Dev", "Abhay", "Raj", "Harsh", "Jai", "Arnav", "Tanish", "Tanmay", "Nikhil",
"Mohit", "Adarsh", "Uday", "Parth", "Ishaan", "Kunal", "Samar", "Saurabh", "Shreyas", "Ankit",
"Armaan", "Rehan", "Faizan", "Imran", "Danish", "Aman", "Neeraj", "Varun", "Hardik", "Ritesh"]

name = input("What is your name: ").capitalize()

if name in name_list:
    print("Your name is indexed")
elif (name not in name_list):
    print("Your name is not indexed")
    print("Do you want to index your name")
    choice = input("Y/n ")
    if choice.capitalize() == "Y":
        name_list.append(name)
    else: pass
else: print("INVALID")

'''
Write a program to calculate the grade of a student from his marks from the
following scheme:
90 - 100 => Ex
80 - 90  => A
70 - 80  => B
60 - 70  => C
50 - 60  => D
<50      => F
'''
# Here I will take percentage from second question as a input

if percentage <= 90:
    print(f"{student_name} has grade Ex")
elif percentage <= 80:
    print(f"{student_name} has grade A")
elif percentage <= 70:
    print(f"{student_name} has grade B")
elif percentage <= 60:
    print(f"{student_name} has grade C")
elif percentage <= 50:
    print(f"{student_name} has grade F")
else: print("FAILED")

# Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Summit your post here:  ").lower()

if "harry" in post:
    print("Harry is mentioned")
else: print("No Harry")

