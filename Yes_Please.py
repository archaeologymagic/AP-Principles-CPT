# Libraries
import random
import time

# Starting Variables
agreements_per_yes = 1 #Starting amount of agreements for every yes that is typed.
agreements = 0
is_shop = False
is_started = False
# This decides whether the game itself has started, like when you skip the tutorial

upgrades = {
    "obedient man": 10,
    "yes please" : 20,
    "yes day" : 40,
    "expert yesser" : 80,
    "never-say-never" : 160,
    "yes god" : 320,
#These upgrades help yes production faster by making auto generating yes' and extra yes' per click
}

owned_upgrades = {
    "obedient man": 0,
    "yes please" : 0,
    "yes day" : 0,
    "expert yesser" : 0,
    "never-say-never" : 0,
    "yes god" : 0,
#These are all the upgrades owned by the player, they can be bought with agreements
}

valid_words = ["yes", "shop", "close"]
valid_upgrades = []

def response_check(a):
    if a in valid_words:
        return a
    else:
        return False
    
#This checks which words are ok for the user to say, like for the shop or to close it
def has_upgrade(a):
     for i in owned_upgrades:
        if i == a:
            return True
        else:
            print("Try again!")
#This section of code defines whether the player is opening or clsoing the shop
def shop(a):
    for x, y in a.items():
        print(x," : ", y)

# Tutorial
is_tutorial = input("Would you like a tutorial (y/n) ? \n")
is_tutorial = is_tutorial.lower()
if is_tutorial == "yes" or is_tutorial == "y" and is_started == False:
    while agreements == 0:
        if response_check(input("Type yes to get an agreement. \n")) == "yes":
            agreements += agreements_per_yes
            print(agreements)
    print("Task: Get 10 Agreements!")
    while agreements < 10:
            if response_check(input("Type yes to get agreements! \n")) == "yes":
                agreements += agreements_per_yes
                print(agreements)
    print("Well Done!") # Text to instruct player
    time.sleep(1) # Delay in seconds
    print("You can use your agreements to purchase upgrades \n to get more agreements with each yes!") 
    time.sleep(1)
    print("You can open the store by typing shop!")
    time.sleep(1)
    #The tutorial teaches you some of the basics like typing yes and agreements. It a
    while shop == False:
        if response_check(input("Open the shop!")) == "shop":
            is_shop = True
    if is_shop == True:
        shop(upgrades)
        



    is_started = True


elif is_tutorial == "no" or is_tutorial == "n" and is_started == False:
    print("You skipped the tutorial")
    is_started == True
#Code that decides whether the tutorial has been skipped

# Game Loop / Main Game
# input

 