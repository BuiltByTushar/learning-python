# If, elif and else 

condition_1 = 1
condition_2 = 0


user_input = int(input("1 or 0 :--> "))
if (user_input == condition_1):
    print("sucess1")
elif (user_input == condition_2):
    print("sucess2")
else : print("sucess3")



age = int(input("What is your Age?  ->"))

if (age >= 18):
    print("wellcome")
elif (age < 0):
    print("INVALID age: negative ages do not exist")
elif (age == 0):
    print("Are you sure that is your age and not numbers of times you have touched GRASS")
else: print("You are underaged")
