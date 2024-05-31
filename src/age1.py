'''
Created on Sep. 26, 2023
Asks the user for a character and their age then responds with whether Frodo is older or younger than them
@author: Sebastian
'''
frodo_age = 51

name = input("What is the name of the character?: ")
age = int(input(f"How old is {name}?: "))

if age<frodo_age :
    print(f"{name} is {age} years old, and they are younger than Frodo")
elif age == frodo_age:
    print(f"{name} is {age} years old, and they are the same name as Frodo")
else : #since both other cases have been checked, this only runs when age>frodo_age
    print(f"{name} is {age} years old, and they are older than Frodo")
