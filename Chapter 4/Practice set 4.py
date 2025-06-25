# Write a program to store seven fruits in a list entered by the user.
Fruits = []
x = 1
while ( x < 7):
    Fruits.append(input("Type Name of a Fruit:  -->"))
    x+=1
print(Fruits)

# Write a program to accept marks of 6 students and display them in a sorted manner

M1 = int(input("marks of student of roll no. 1: -->"))
M2 = int(input("marks of student of roll no. 2: -->"))
M3 = int(input("marks of student of roll no. 3: -->"))
M4 = int(input("marks of student of roll no. 4: -->"))
M5 = int(input("marks of student of roll no. 5: -->"))
M6 = int(input("marks of student of roll no. 6: -->"))
Student_list = [M1, M2, M3, M4, M5, M6]  #Making it a list insed of tuple to sort
 
Student_list.sort(reverse=True) 
print(Student_list)

# Check that a tuple type cannot be changed in python.
# I khows

# Write a program to sum a list with 4 numbers.
list = [3, 2, 4, 1]
print(list[0]+list[1]+list[2]+list[3])
# OR !!
print(sum(list))
# Write a program to count the number of zeros in the following tuple:

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))