'''
Created on Sep. 26, 2023
Asks for a characters age and list all the characters older and younger
@author: Sebastian
'''

pippin_age = 29
frodo_age = 51
gollum_age = 589
arwen_age = 2901

name = input("What is the name of the character?: ")
age = int(input(f"How old is {name}?: "))

list_younger = "" #the list of characters of whom the character is younger than
list_older = "" #the list of characters of whom the character is older than

if age<0 :
    print("Invalid age")
elif age < pippin_age : #pippin is youngest so all will be older
    list_younger += "Arwen, Gollum, Frodo, Pippin."
elif age < frodo_age : #being an elif, only happens if older than pippin removing the need for that check
    list_older += "Pippin."
    list_younger += "Arwen, Gollum, Frodo." 
elif age < gollum_age : #like above, the elif removes having to check for the who is younger than the character
    list_older += "Frodo, Pippin."
    list_younger += "Arwen, Gollum"
elif age < arwen_age : 
    list_older += "Gollum, Frodo, Pippin."
    list_younger += "Arwen."
else :
    list_older += "Arwen, Gollum, Frodo, Pippin."

if list_older != "" : #only runs this segment if the list isn't empty
    print(f"{name} is {age} years old, and they are older than {list_older}")    
if list_younger != "" : #only runs this if the list isn't empty
    print(f"{name} is {age} years old, and they are younger than {list_younger}")
