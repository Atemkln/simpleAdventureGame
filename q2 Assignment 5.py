"""
This program is a text-based adventure game.
Author: Adam Kline
Student Number: 20177124
Date: February 12th, 2021
"""
import random  # for the dice game


"""
This function is used to allow the user to make the choice of where to go, location-wise.
"""
def road_fork(name):  # the starting point for the choices of location
    print(f'The road up ahead diverges into three directions. The signs say: "Inn 20 miles" on one path, and "Bridge 30'
      ' miles" on the other.')
    print('The final path is a toll-booth with a mean-looking guard standing in front of it. Which '
      f'path will you choose to take, {name}?')
    print("Input 'a' to head to the Inn, 'b' to opt for the bridge, and 'c' to try your luck with the guard.")
    choice = ""
    while choice != "a" and choice != "b" and choice != "c":
        choice = input("Please enter your choice (either 'a', 'b', or 'c') for where to go (remember you can "
                       "always come back here): ")
    if choice == "a":
        inn_place()
    elif choice == "b":
        bridge_place()
    elif choice == "c":
        toll_place()


"""
This function initializes the inn-setting.
"""
def inn_place():  #
    print("You decide to head for the inn.")
    print("""After a bit of walking you finally arrive at "The Bee's Knees" bar and grill.""")
    print("The bartender gives you a toothless grin, and you see a few people playing dice in the corner.")
    inn_selection()


"""
This function is what controls the users choices at the inn
"""
def inn_selection():
    print("Input 'a' to speak to the bartender, 'b' to play some dice, and 'c' to head back to the fork in the road.")
    inn_choice = ""
    while inn_choice != "a" and inn_choice != "b" and inn_choice != "c":
        inn_choice = input("Please enter your input (either 'a', 'b' or 'c') to make your choice: ")
    if inn_choice == "a":
        print("After sweet-talking him into giving you a dwarven ale on the house, you have a pleasant chat with "
              "the bartender.")
        print("He gives you dental hygeine advice. You probably won't take it.")
        inn_selection()
    elif inn_choice == "b":
        print("Time to play some dice!")
        dice_roll = random.randint(1, 7)  # gets a random value for the dice
        str_dice_roll = str(dice_roll)  # converts the number into a string
        print("Pick a number between from 1 to 6, and if it matches the dice roll, you win!")
        dice_pick = ""
        while dice_pick != "1" and dice_pick != "2" and dice_pick != "3" and dice_pick != "4" and dice_pick != "5" and dice_pick != "6":
            dice_pick = input("Please enter your choice (must be a number between 1 and 6): ")
        if dice_pick == str_dice_roll:
            print("You win! (You don't win money, but they certainly have more respect for you now).")
            inn_selection()
        else:
            print("Ooh sorry, better luck next time. Respect for you has been lost.")
            inn_selection()
    else:
        road_fork(name)


"""
This function initializes the bridge setting
"""
def bridge_place():
    print("You decide to head for the bridge.")
    print("After a bit of walking you find yourself standing in front of a perilous drawbridge overlooking a cliff.")
    print("A wizened old woman stands at the entrance of it, blocking your path.")
    print("You get a whiff of napalm and fire as you gaze upon the crease underneath the bridge.")
    bridge_selection(name)


"""
This function regulates user choices at bridge setting
"""
def bridge_selection(name):
    print("Input 'a' to speak to the old woman and 'b' to head back to the fork in the road.")
    bridge_choice = ""
    while bridge_choice != "a" and bridge_choice != "b":
        bridge_choice = input("Please enter your input (either 'a', 'b') to make your choice: ")
    if bridge_choice == "a":
        print("The old woman grins at you as you step up to face her.")
        print('"Only those who answer my question may pass," she says.')
        print('She reads from a scroll: "Suppose there are 49 dogs signed up to compete in the dog show. There are 36 '
              'more small dogs than big dogs signed up in the show. How many small dogs are signed up to compete?"')
        print(f"{name}, you must answer correctly in order to pass! Input your answer underneath in the form of a "
              f"number. Good luck.")
        number_of_small_dogs = "42.5"
        answer = input("Please enter the number of small dogs competing: ")
        if number_of_small_dogs == answer:
            print('"Correct!", says the old woman. "But, I am still not going to let you pass. Take it up with'
                  ' my supervisor or something."')
            print(f"Well, {name}, looks like you can't win them all.")
            bridge_selection(name)
        else:
            print('"Haha! Incorrect. Try again if you dare," she says.')
            bridge_selection(name)
    else:
        road_fork(name)


"""
This function initializes toll setting
"""
def toll_place():
    print("You decide to try to talk to the guard in the booth.")
    print("As you walk up, the guard gives you a menacing glare from behind the newspaper he is reading. Not too"
          " friendly it seems.")
    toll_selection(name)


"""
This function regulates choices in the toll setting
"""
def toll_selection(name):
    print("Input 'a' to speak to the guard, 'b' to try and run past him, and 'c' to head back to the fork in the road.")
    toll_choice = ""
    while toll_choice != 'a' and toll_choice != 'b' and toll_choice != 'c':
        toll_choice = input("Please enter your input (either 'a', 'b') to make your choice: ")
    if toll_choice == 'a':
        print('"What do you want?" the guard says gruffly. You give him your name and he sneers at you as he'
              ' checks his list.')
        print(f'He puts the list down. "Yeah no, I am not seeing any {name} on this list. You are not'
              f' getting past me today, pipsqueak."')
        print("It appears as though the diplomatic approach will not work here.")
        toll_selection(name)
    elif toll_choice == 'b':
        print("You take off, zooming past him, the wind whipping through your hair. All that training in the "
              "village cross-country team did wonders for your 400-metre sprint.")
        print("It's strange, but the guard makes no attempt to catch you.")
        print("After running for a while, you begin to approach a certain fork in the road that looks oddly familiar..."
              "")
        road_fork(name)
    else:
        road_fork(name)



print('"And stay out!"')
print("You remember the last words the mayor of your village screamed at you before an angry mob slammed the gates "
      "in your face.")
print("You just had to pull that stupid stunt at the Twilight Festival didn't you?")
print("Ah, anyways Listener, what is your name again?")
name = input("Enter your name: ")  # user enters name for the game
print(f"Oh yes, I remember you now, you're {name}.")
print(f"Well then, {name}, what will you do now? You don't have a single penny to your name, let alone friends"
      f" or family. The world is essentially your oyster.")
road_fork(name)





