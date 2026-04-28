# Libraries
import random
import time
import math

# Starting Variables
agreements_per_yes = 1 #Starting amount of agreements for every yes that is typed.
agreements = 0
is_shop = False
is_started = False
# This decides whether the game itself has started, like when you skip the tutorial

upgrades = {
    "obedient man": 10,
    "yes please" : 75,
    "yes day" : 500,
    "expert yesser" : 1000,
    "never-say-never" : 3000,
    "yes god" : 5250,
#This dictionary includes the costs of the upgrades
}

owned_upgrades = {
    "obedient man": 0,
    "yes please" : 0,
    "yes day" : 0,
    "expert yesser" : 0,
    "never-say-never" : 0,
    "yes god" : 0,
#This is the amount of the upgrade that the player owns
}


upgrade_multiplier = {
    "obedient man": 1,
    "yes please" : 5,
    "yes day" : 10,
    "expert yesser" : 20,
    "never-say-never" : 40,
    "yes god" : 50,
#These is the multiplier of all the upgrades

}

valid_words = ["yes", "shop", "close"]
    
def upgrade_adder(a): #This function is used to add upgrades to the player
    global agreements_per_yes
    global agreements
    global is_shop
    #Using global allows the variables to be changed in the function
    
    if a in upgrades:
        multi = upgrade_multiplier[a]
        cost = upgrades[a]
        if agreements >= cost:
            agreements_per_yes += multi
            agreements -= cost #Removes the cost from the agreements.
            owned_upgrades[a] += 1 #Adds one to the owned upgrades count
            upgrades[a] += math.ceil(upgrades[a] * 0.25) #Increases the price by 0.25 and rounds it up to the nearest integer
            print("You own", owned_upgrades[a], a)
        else:
             print("You are too poor for this...")
    elif a == "close":
        is_shop = False
    else: 
        print("Not found")
    
def shop(a): #Prints the upgrades dictionary
    for x, y in a.items():
        print(x," : ", y)

def response_check(a): #Checks if the response is valid and acts upon it
    global agreements
    global agreements_per_yes
    global is_shop
    a = a.lower() #sets input to lowercase to make it easier to check what was inputted
    if a in valid_words:
        if a == "shop":
            is_shop = True
            shop(upgrades)
            # Sets is shop to true and prints the shop out if the inputted word is shop
        elif a == "close":
            is_shop = False
            # Sets is_shop to false if the input if close
        elif a == "yes":
            agreements += agreements_per_yes

            print("\n", agreements, "\n")
            # adds to the players agreements based on their current multiplier and prints their agreements if the input is yes
    else:
        return False
#This checks which words are ok for the user to say, like for the shop or to close it



# Tutorial
is_tutorial = input("Would you like a tutorial (y/n) ? \n").lower()

if is_tutorial == "y" or "yes":

    while agreements == 0: #Runs as long as the player has zero agreements
        response_check(input("Type yes to get an agreement. \n")) #Calls the response check function which uses an algorithm to check what should be done based on the response.
    
    print("Task: Get 10 Agreements!")

    while agreements < 10: #Runs until the player has over 10 agreements
            response_check(input("Type yes to get agreements! \n"))

    print("Well Done!") # Text to instruct player
    time.sleep(1) # Delay in seconds

    print("You can use your agreements to purchase upgrades \n to get more agreements with each yes!") 
    time.sleep(1)

    while is_shop == False:  #Runs while is shop is false
        print("You can open the store by typing shop! \n")
        time.sleep(1)
        response_check(input("Open the shop! \n")) 

    while owned_upgrades["obedient man"] == 0:  #Runs while the obedient man upgrade is not owned.
        if is_shop == True:
            upgrade_adder(input("Now purchase the Obedient Man upgrade by typing: obedient man! \n"))
    
    while is_shop == True:
        response_check(input("Type 'close' to close the shop!: \n"))
    
    print("Now close the shop! \n")  
    time.sleep(0.5)

    print("Well Done!")
    time.sleep(0.5)

    print("You have finished your training! \n")
    is_started = True #Starts the main loop

elif is_tutorial == "n" or "no":
    print("You skipped the tutorial")
    is_started = True #Starts the main loop
#Code that decides whether the tutorial has been skipped


# Game Loop / Main Game
print("Begin!")
while is_started == True: # Runs as long as is_started is true
    response_check(input("\n \n")) #Calls the response check function and adds 2 empty lines
    if is_shop == True: #Checks if the shop should be opened
        upgrade_adder(input("What do you want to buy? (Remember to close the shop!): \n"))  #Checks if the input is a valid upgrade and adds it to the player.   
