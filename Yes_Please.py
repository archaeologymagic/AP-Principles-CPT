# Libraries
import random
import time

# Starting Variables
agreements_per_yes = 1
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

valid_words = ["yes", "shop"]
owned_upgrades = {}

def response_check(a):
    for i in valid_words:
        if i == a:
         return i
    else:
        return False

def has_upgrade(a):
     for i in owned_upgrades:
        if i == a:
            return a
        else:
            return False

# def shop(a):
   # for x, y in a:
     #   print(x," : ", y)

# Tutorial
is_tutorial = input("Would you like a tutorial (y/n) ? \n")
is_tutorial = is_tutorial.lower()
if is_tutorial == "yes" or is_tutorial == "y" and is_started == False:
    while agreements == 0:
        if response_check(input("Type yes to get an agreement. \n")) == "yes":
            agreements += 1
    print(agreements)
    print("Task: Get 10 Agreements!")
    while agreements < 10:
            if response_check(input("Type yes to get agreements! \n")) == "yes":
                agreements += 1
                print(agreements)
    print("Well Done!") # Text to instruct player
    time.sleep(1) # Delay in seconds
    print("You can use your agreements to purchase upgrades \n to get more agreements with each yes!") 
    time.sleep(1)
    print("You can open the store by typing shop!")
    time.sleep(1)
    #The tutorial teaches you some of the basics like the delay between typing yes' and how you need to type 10 yes'. The code displays messages to guide the player so they aret confused on what  Once you get to 10 agreements, the tutoial wille end and begin the accual game.
    
    while not has_upgrade("obedient man"):
        if response_check(input("Open the shop!")) == "shop":
            is_shop == True
            shop(upgrades)

            


            
    
    
    is_started = True


elif is_tutorial == "no" or is_tutorial == "n" and is_started == False:
    print("You skipped the tutorial")
    is_started == True
#Code that decides whether the tutorial has been skipped

# Game Loop / Main Game
# input

