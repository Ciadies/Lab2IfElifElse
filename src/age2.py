'''
Created on Sep. 26, 2023
Asks for a character's age and responds with their age relative to Frodo and Gollum
@author: Sebastian
'''
frodo_age = 51
gollum_age = 589

name = input("What is the name of the character?: ")
age = int(input(f"How old is {name}?: "))

if age<frodo_age :
    print(f"{name} is {age} years old, and they are younger than Frodo and Gollum")
elif age>frodo_age and age<gollum_age :
    print(f"{name} is {age} years old, and they are older than Frodo and younger than Gollum")
else  :
    print(f"{name} is {age} years old, and they are older than Frodo and Gollum")