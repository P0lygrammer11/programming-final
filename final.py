# AL, EG, JT , NS
#invintory
#NS
invintntory = []
#items
#NS
items = 0
#moves
moves = 0
#game stats
saved_file = "game_stats.txt"
#file for the starts
# NS
with open ("game_stats.txt", "r") as file:
    saved_stats = file.read().split(",")
win = int(saved_stats[0])
loss = int(saved_stats[1])
#functions for room 1
def room1(invintory):
    print("you are in the classroom")
    print("the north door is locked")

    if "key" in invintory:
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
                current_room = "room3"
            elif choice_room1 == "3":
                print("Inventory:", invintory)
                input("Press Enter to continue...")
                current_room = "room1"
            elif choice_room1 == "4":
                print("The north door is locked.")
                current_room = "room1"
            else:
                print("Invalid choice. Please try again.")

#functions for room 2
#functions for room 3
#functions for room 4
#functions for room 5
#functions for room 6
#game function
# game starting 
 if __name__ == "__main__":
     main()

    
