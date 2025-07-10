# Question 1. 
# Write a program to print Twinkle twinkle little star poem in python

print(''' Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')

# Question 3.
# Install an external module and use it to perform an operation of your interest.


import wikipedia

result = wikipedia.page("Minecraft")

print(result.summary)

# Question 4. 
# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that

import os

# it is used to set the location 
path = "C://Users//pogbo//Downloads"
dir_list = os.listdir(path)
# just some Extra for intex
print("print files and directories in '", path, "' :")
# now we print the list
print(dir_list)