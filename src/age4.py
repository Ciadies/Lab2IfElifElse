'''
Created on Sep. 26, 2023

@author: Sebastian
'''
names = [
    "Frodo",
    "Samwise",
    "Gandalf",
    "Legolas",
    "Gimli",
    "Aragorn",
    "Boromir",
    "Merry",
    "Pippin",
]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]

char_name = input("What is the name of the character?: ")
char_age = int(input(f"How old is {char_name}?: "))

list_younger = ""
list_older = ""

for idx in range(len(ages)) :
    
    if char_age < ages[idx] :
        list_younger += " " + names[idx] + ","
    else :
        list_older += " " + names[idx] + ","
list_older = list_older[0:-1]  
list_younger = list_younger[0:-1]      
if list_older != "" : #only runs this segment if the list isn't empty
    print(f"{char_name} is {char_age} years old, and they are older than{list_older}.")    
if list_younger != "" : #only runs this if the list isn't empty
    print(f"{char_name} is {char_age} years old, and they are younger than{list_younger}.")