# AL, EG, JT , NS
#game loading screen



# inventory
#NS
inventory = []
#items
#NS
items = 0
#moves
moves = 0
#game stats
saved_file = "game_stats.txt"
#file for the stats
# NS
with open ("game_stats.txt", "r") as file:
    saved_stats = file.read().split(",")
win = int(saved_stats[0])
loss = int(saved_stats[1])
#functions for room 1
def room1(invintory):
    print("you are in the classroom")
    print("the north door is locked")

    if "key" in inventory:
        print("you can use the key to unlock the north door")
    else:
        while True:
            print("What do you want to do?")
            print("1. Solve the puzzle")
            print("2. Look around the classroom")
            print("3. Check inventory")
            print("4. Go north")
            choice_room1 = input("Enter your choice: ")
            if choice_room1 == "1":
                key_puzzle = input("Solve this puzzle to get the master key: What has keys but can't open locks? ")
                if key_puzzle.lower() == "piano":
                    print("You solved the puzzle and obtained the master key!")
                    invintory.append("master key")
                    break
                else:
                    print("Incorrect answer. You cannot get the master key.")
                    retry_puzzle = input("Do you want to try the puzzle again? (yes/no) ")
                    if retry_puzzle.lower() != "yes":
                        break
            elif choice_room1 == "2":
                print("You look around the classroom but suddenly hear a few steps behind you.")
                print("You quickly turn around but see no one there.")
                print("The classroom feels eerie and quiet after that.")
                print("You feel a chill run down your spine.")
                print("You can't shake off the feeling that someone is watching you.")
                print("You decide to stay alert and proceed with caution.")
                print("You continue to search the classroom carefully, hoping to find any clues or useful items.")
                print("Despite the eerie feeling, you manage to find a small key hidden under a desk.")
                invintory.append("key")
                print("You put the key into your inventory.")
                print("You feel a sense of accomplishment for finding the key.")
                print("You decide to keep searching the classroom for any other hidden items.")
                print("However, you don't find anything else of interest.")
                print("you leave the classroom with happiness for finding the key.")
                current_room =  "room3"
                break
            elif choice_room1 == "3":
                print("Inventory:", invintory)
                input("Press Enter to continue...")
                current_room = "room1"
                break
            elif choice_room1 == "4":
                print("The north door is locked.")
                current_room = "room1"
            else:
                print("Invalid choice. Please try again.")
#EG
#functions for room 2
def room2(inventory):
    print("you are in the hallway, but freedom is far away. Guarding the corridor are the dreaded Trip")
    print("you look around, but you recognize nothing that looks fimliar ")
    print("you see a door at th end of the hallway")
    print("as you keep walking towards the invintory, you hear something from the south classroom ")
    while True:
        print("where do you wanna go?")
        print("(1) go to the south classroom")
        print("(2) go to the door at the end of the hallway")
        print("(3) go back to the the classroom")
        choice_room2 = input("enter your choice: ")
        if choice_room2 == "1":
            print("you walk back after hearing the sounds, hoping to find someone or something")
            print("unfotnately theres nothing in this room except a flahslight")
            flashlight_room2= input ("do you wanna (1) grab the flashlight or (2)leave the flashlight and go back to the hallway")
            if flashlight_room2 == "1":
                inventory.append("flashlight")
                break
            if flashlight_room2 == "2":
                return room2
            else:
                print("please eneter actual things:))")
                break
        if choice_room2 == "2":
            if "hallway_key" in inventory :
                print("you have the key you may go inisde ")
                current_room = "room5"
                break
            else:
                key_room2 = input("uh-oh you dont have a key do you wanna go to room 1 to get a key?(y/n)").strip().lower()
                if key_room2 == "y" or "yes":
                    current_room = room1
                if key_room2 == "n":
                    print("great, you're still stuck here")
                    return room2
                else:
                    print("idk, man do smt pls")
                    break
        if choice_room2 == "3":
            print("you go back to the classroom")
            current_room = "room1"
            break
#functions fo
#NS
def room3(inventory):
    print("you are in the halway, but freedom is far away. Guarding the corridor are the dreaded Trip")
    print("you look around, but you recognize nothing that looks fimliar ")
    print("you see a door at th end of the hallway")
    print("as you keep walking towards the invintory, you hear something from the south classroom ")
    while True:
        print("where do you wanna go?")
        print("(1) go to the south classroom")
        print("(2) go to the door at the end of the hallway")
        print("(3) go back to the the classroom")
        choice_room3 = input("enter your choice: ")
        if choice_room3 == "1":
            print("you walk back after hearing the sounds, hoping to find someone or something")
            print("unfotnately theres nothing in this room except a flahslight")
            flashlight_room3= input ("do you wanna (1) grab the flashlight or (2)leave the flashlight and go back to the hallway")
            if flashlight_room3 == "1":
                inventory.append("flashlight")
                break
            if flashlight_room3 == "2":
                return room3
            else:
                print("please eneter actual things:))")
                break
        if choice_room3 == "2":
            if "hallway_key" in inventory :
                print("you have the key you may go inisde ")
                current_room = "room5"
                break
            else:
                key_room3 = input("uh-oh you dont have a key do you wanna go to room 1 to get a key?(y/n)").strip().lower()
                if key_room3 == "y" or "yes":
                    current_room = room1
                if key_room3 == "n":
                    print("great, you're still stuck here")
                    return room3
                else:
                    print("idk, man do smt pls")
                    break
        if choice_room3 == "3":
            print("you go back to the classroom")
            current_room = "room1"
            break
        else:
            break
#functions for room 4
#AL
def room4(inentory):
    print("The sad truth is that the exit door is not near and you have to face idk Queen Elizabeth II")
    while True :    
        choice_room4 = ("What you want to do (1)Throw her beascuits with acid (2) Blow her up to reduce her to ashes (3) Kick her to the Big Ben")
        if choice_room4 == "1":
            print("It worked !! The Queen is gonne, but so is part of the floor")
            print("Sadly you will lose points for that")
        elif choice_room4 == "2" :
            print("Surprisingly the queen disappeared within the air.")
            print("And between the ashes remaining, you find a royal key that the queen kept.")
            print("It might be useful later.")        
        elif choice_room4 == "3" : 
            print("What a horrible idea.")
            print("Despite the Queen seem like a raisin, her weigth is enough to keep her from flying across an ocean.")
            print("She kick you out of the room, so you need yo restart")
            return room4 
#function for room 5    
#JT   
def room5(inventory)
    print("You find yourself surrounded by mushrooms.")
    print("There is a red and white mushrooms taubting you to eat.")
    print("You haven't eaten in so long you are starving." )
    print("You want to eat it put there is something wrong with it")
    while True:
        print("What do you wan't to do.")
        print ("(1) Eat the mushroom maybe it will give you super powers.")
        print("(2) Leave it behind it's too creepy")
        print("(3)Store it in your inventory it might be usful latter")
        choice1_room5 = input("Enter your choice:")
        if choice1_room5 == "1":
            print("You eat it, you wait for something but notthing happens so you start your journy through Room 5.")
            print("You find a massive castle in the distance. It looks beautiful, the windows blind you dispite your distance")
            print("You tred forward. As walking you hear something in the distance it sounds like a yell of joy.")
            print("It gets louder and louder but it just stops.")
            print("That sound terrifies you.")
            print("You want to find shelter but you also feel it would be safe to keep moving.")
            
        choice2_room5 = 

#functions for room 6
#game function
# game starting 

