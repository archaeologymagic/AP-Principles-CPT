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
#These upgrades help yes production faster by making auto generating yes' and extra yes' per click. They are buyable by typing "shop"
}

owned_upgrades = {
    "obedient man": 0,
    "yes please" : 0,
    "yes day" : 0,
    "expert yesser" : 0,
    "never-say-never" : 0,
    "yes god" : 0,
#These upgrades help yes production faster by making auto generating yes' and extra yes' per click
}


upgrade_multiplyer = {
    "obedient man": 1,
    "yes please" : 5,
    "yes day" : 10,
    "expert yesser" : 20,
    "never-say-never" : 40,
    "yes god" : 50,
#These are all the upgrades owned by the player, they can be bought with agreements. These upgrades can buff the amount of agreements a player can get at a time

}

valid_words = ["yes", "shop", "close"]
valid_upgrades = []
    
def upgrade_adder(a):
    global agreements_per_yes
    global agreements
    multi = upgrade_multiplyer[a]
    cost = upgrades[a]
    if a in upgrades:
        if agreements >= cost:
            agreements_per_yes += multi
            agreements -= cost
            owned_upgrades[a] += 1
        else:
             return 0
    else: 
        return 0
    
def shop(a):
    for x, y in a.items():
        print(x," : ", y)
#This section of code defines whether the player is opening or clsoing the shop

def response_check(a):
    global agreements
    global agreements_per_yes
    global is_shop
    a = a.lower()
    if a in valid_words:
        if a == "shop":
            is_shop = True
            shop(upgrades)
        elif a == "yes":
            agreements += agreements_per_yes
            print(agreements)
    else:
        return False
#This checks which words are ok for the user to say, like for the shop or to close it



# Tutorial
is_tutorial = input("Would you like a tutorial (y/n) ? \n")
is_tutorial = is_tutorial.lower()
if is_tutorial == "yes" or is_tutorial == "y" and is_started == False:
    while agreements == 0:
        response_check(input("Type yes to get an agreement. \n"))
    print("Task: Get 10 Agreements!")
    while agreements < 10:
            response_check(input("Type yes to get agreements! \n"))
    print("Well Done!") # Text to instruct player
    time.sleep(1) # Delay in seconds
    print("You can use your agreements to purchase upgrades \n to get more agreements with each yes!") 
    time.sleep(1)
    #The tutorial teaches you some of the basics like typing yes and agreements. It a
    while is_shop == False:
        print("You can open the store by typing shop! \n")
        time.sleep(1)
        response_check(input("Open the shop!"))
    if is_shop == True:
        shop(upgrades)
        while owned_upgrades["obedient man"] == 0:
            upgrade_adder(input("Now purchase the Obedient Man upgrade by typing: obedient man!"))
    is_started = True


elif is_tutorial == "no" or is_tutorial == "n" and is_started == False:
    print("You skipped the tutorial")
    is_started == True
#Code that decides whether the tutorial has been skipped


# Game Loop / Main Game
# input