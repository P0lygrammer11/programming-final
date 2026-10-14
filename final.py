# AL, EG, JT, NS
# HORROR ADVENTURE GAME


print("=" * 30 + " W E L C O M E " + "=" * 30)


# GAME DATA

inventory = []
saved_file = "game_stats.txt"

# Read the saved game stats
with open(saved_file, "r") as file:
    saved_stats = file.read().split(",")

wins = int(saved_stats[0])
losses = int(saved_stats[1])

# AL, EG, JT, NS
# HORROR ADVENTURE GAME


print("=" * 30 + " W E L C O M E " + "=" * 30)


# GAME DATA

def save_game_stats():
    # Save the total wins and losses so they remain after the game closes.
    with open(saved_file, "w") as file:
        file.write(f"{wins},{losses}")


def show_inventory():
    # Display the items the player has collected.
    if inventory:
        print("Inventory:", ", ".join(inventory))
    else:
        print("Your inventory is empty.")


# ROOM 1: CLASSROOM
# AL: Classroom puzzle and key system


def room1():
    print("\n--- ROOM 1: CLASSROOM ---")
    print("You are in an abandoned classroom.")
    print("The north door is locked.")

    while True:
        print("\n1. Solve the puzzle")
        print("2. Look around the classroom")
        print("3. Check inventory")
        print("4. Go north")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            answer = input(
                "What has keys but cannot open locks? "
            ).strip().lower()

            if answer == "piano":
                print("Correct! You found the master key.")
                if "master key" not in inventory:
                    inventory.append("master key")
                else:
                    print("You already have the master key.")
            else:
                print("Wrong answer! Try again.")

        elif choice == "2":
            if "key" in inventory:
                print("You have already searched this classroom.")
            else:
                print("You hear footsteps behind you...")
                print("You turn around, but nobody is there.")
                print("Under a desk, you discover a small key!")
                inventory.append("key")

        elif choice == "3":
            show_inventory()

        elif choice == "4":
            if "master key" in inventory:
                print("The master key unlocks the north door!")
                return "room2"
            else:
                print("The door needs the master key.")
                print("Solve the puzzle to obtain it.")

        else:
            print("Invalid choice. Try again.")


# ROOM 2: HALLWAY
# EG: Hallway exploration and key collection


def room2():
    print("\n--- ROOM 2: HALLWAY ---")
    print("A dark hallway stretches before you.")
    print("You hear something moving in the south classroom.")

    while True:
        print("\n1. Enter the south classroom")
        print("2. Go to the door at the end")
        print("3. Return to the classroom")
        print("4. Check inventory")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nYou enter the south classroom.")

            if "flashlight" not in inventory:
                print("You find a flashlight and a hallway key!")
                inventory.append("flashlight")
                inventory.append("hallway_key")
            else:
                print("The classroom is empty.")

        elif choice == "2":
            if "hallway_key" in inventory:
                print("You unlock the door and enter.")
                return "room4"
            else:
                print("The door is locked.")
                print("Search the south classroom for a key.")

        elif choice == "3":
            return "room1"

        elif choice == "4":
            show_inventory()

        else:
            print("Invalid choice. Try again.")


# ROOM 4: JANITOR'S ROOM
# EG: Janitor encounter and player choices


def room4():
    print("\n--- ROOM 4: JANITOR'S ROOM ---")
    print("You enter a room near the exit.")
    print("Suddenly, the old janitor appears!")
    print('"Why are you not in class?" he demands.')
    print("You must act quickly!")

    while True:
        print("\n1. Throw a bucket of water")
        print("2. Throw a book")
        print("3. Run back to the hallway")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("The janitor slips on the wet floor!")
            print("You escape, but make a terrible mess.")
            print("You lose one point... just kidding!")
            return "room5"

        elif choice == "2":
            print("The book hits the janitor.")
            print("He falls asleep, dropping a strange key!")
            print("You pick up the janitor key.")

            if "janitor key" not in inventory:
                inventory.append("janitor key")

            return "room5"

        elif choice == "3":
            print("You run back to the hallway.")
            return "room2"

        else:
            print("Choose 1, 2, or 3.")


# ROOM 5: MUSHROOM FOREST
# JT: Mushroom choices and the lose condition


def room5():
    print("\n--- ROOM 5: MUSHROOM FOREST ---")
    print("You find yourself surrounded by mushrooms.")
    print("A strange red-and-white mushroom catches your eye.")
    print("In the distance, you see a beautiful castle.")
    print("Suddenly, a mysterious scream echoes through the forest!")

    while True:
        print("\n1. Eat the mushroom")
        print("2. Leave it and keep moving")
        print("3. Store the mushroom")
        print("4. Check inventory")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("You eat the mushroom...")
            print("Everything spins, and you collapse!")
            print("GAME OVER!")
            return "game_over"

        elif choice == "2":
            print("You wisely leave the mushroom alone.")
            print("You follow a path toward the dark forest.")
            return "room6"

        elif choice == "3":
            if "mushroom" not in inventory:
                inventory.append("mushroom")
                print("You carefully store the mushroom.")
            else:
                print("You already have a mushroom.")

        elif choice == "4":
            show_inventory()

        else:
            print("Invalid choice. Try again.")


# ROOM 6: DARK FOREST
# JT: Forest exploration and path choices


def room6():
    print("\n--- ROOM 6: DARK FOREST ---")
    print("The trees are tall and twisted.")
    print("Fog covers the ground.")
    print("You hear growling somewhere behind you.")

    if "flashlight" in inventory:
        print("Your flashlight helps you see a hidden path.")
    else:
        print("You struggle to see through the darkness.")

    while True:
        print("\n1. Explore the forest")
        print("2. Search for an exit")
        print("3. Check inventory")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Glowing eyes appear between the trees!")
            print("You run before the creature catches you.")
            print("You discover a path leading to a castle.")
            return "finalroom7"

        elif choice == "2":
            print("You follow a faint trail through the fog.")
            print("At last, you discover a mysterious door.")
            return "finalroom7"

        elif choice == "3":
            show_inventory()

        else:
            print("Invalid choice. Try again.")


# ROOM 7: FINAL ROOM
# NS: Final escape challenge and win condition


def finalroom7():
    print("\n--- FINAL ROOM ---")
    print("You find a massive door with a keypad.")
    print("A note reads: 'The escape code is 1234.'")

    code = input("Enter the four-digit code: ").strip()

    if code == "1234":
        print("\nThe door opens!")
        print("CONGRATULATIONS! YOU ESCAPED!")
        return "victory"

    else:
        print("\nThe code is incorrect.")
        print("The door locks, and you are trapped!")
        print("GAME OVER!")
        return "game_over"


# MAIN GAME LOOP
# NS: Connect the rooms and update saved game statistics


def game():
    global wins, losses

    inventory.clear()
    current_room = "room1"

    print("\nWelcome to the Horror Adventure Game!")
    print("Find keys, explore rooms, and escape the building.")
    print("Choose a number from each menu to play.")
    print("Collect items, solve puzzles, and avoid danger!")

    while current_room not in ("victory", "game_over", "quit"):

        if current_room == "room1":
            current_room = room1()

        elif current_room == "room2":
            current_room = room2()

        elif current_room == "room4":
            current_room = room4()

        elif current_room == "room5":
            current_room = room5()

        elif current_room == "room6":
            current_room = room6()

        elif current_room == "finalroom7":
            current_room = finalroom7()

        else:
            print("Something went wrong. Returning to the classroom.")
            current_room = "room1"

    # Count the result once after each completed playthrough.
    if current_room == "victory":
        wins += 1
    elif current_room == "game_over":
        losses += 1

    # Save the updated totals so they carry over to future runs.
    if current_room in ("victory", "game_over"):
        save_game_stats()

    print("\n========== GAME STATS ==========")
    print("Wins:", wins)
    print("Losses:", losses)
    print("================================")

    return current_room


# REPLAY MENU
# AL: Allow the player to start another adventure


def start_game():
    while True:
        result = game()

        if result == "victory":
            print("You survived the adventure!")

        elif result == "game_over":
            print("Better luck next time!")

        again = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if again not in ("yes", "y"):
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    start_game()
