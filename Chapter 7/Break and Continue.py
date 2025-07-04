for x in range(50):
    if x == 34:
        break    # Exits the loop right now
    print(x)


for x in range(50):
    if x == 34:
        print("Skip")
        continue    # Skip this iteration
    print(x)