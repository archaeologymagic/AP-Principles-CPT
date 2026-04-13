#Libraries
import random

#Starting Variables
points_per_yes = 1
playing = True
points = 0
upgrades = {
    "Obedient Man": 10,
    "Yes Please" : 20,
}

def is_yes(a):
    if a == "yes":
        points += 1
    else:
        return False



    #Tutorial
is_tutorial = input("Would you like a tutorial? \n")
is_tutorial = is_tutorial.lower()
if is_tutorial == "True" or "Yes":
    input("Type yes to get points! \n")

elif is_tutorial == "False" or "No":
    print("You chose to skip the tutorial")
    is_tutorial= False
