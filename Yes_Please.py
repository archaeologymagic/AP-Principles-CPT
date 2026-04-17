# Libraries
import random
import time

# Starting Variables
agreements_per_yes = 1
playing = True
agreements = 0
is_shop = False
upgrades = {
    "Obedient Man": 10,
    "Yes Please" : 20,

}
owned_upgrades = {}

def is_yes(a):
    if a == "yes":
        return True
    else:
        return False

def has_upgrade(a):
     for i in owned_upgrades:
        if i == a:
            return True
        else:
            return False



# Tutorial
is_tutorial = input("Would you like a tutorial? \n")
is_tutorial = is_tutorial.lower()
if is_tutorial == "true" or "yes" or "y":
    if is_yes(input("Type yes to get agreements! ")):
        agreements += 1
    print(agreements)
    print("Get 10 Agreements!")
    while agreements < 10:
            if is_yes(input("Type yes to get agreements! ")):
                agreements += 1
                print(agreements)
    


    print("Well Done!") # Text to instruct player
    time.sleep(1) # Delay in seconds
    print("You can use your agreements to purchase upgrades to get more agreements with each yes!")
    time.sleep(0.5)
    print("Type 1 at any time to open the shop!")
    time(0.5)
    print("Open the shop and purchase the Obediant Man!")

    while not (has_upgrade("Obedient Man")):
        

elif is_tutorial == "false" or "no" or "n":
    print("You chose to skip the tutorial")
    is_tutorial = False


# Game Loop / Main Game