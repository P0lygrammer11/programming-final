# AL, EG, JT, NS
# HORROR ADVENTURE GAME
import random

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



saved_file = "game_stats.txt"


def load_game_stats():
    file = open(saved_file, "r")
    data = file.read().strip().split(",")
    file.close()

    wins = int(data[0])
    losses = int(data[1])

    return wins, losses


def save_game_stats(wins, losses):
    file = open(saved_file, "w")
    file.write(str(wins) + "," + str(losses))
    file.close()


def get_choice(prompt, choices):
    while True:
        answer = input(prompt).strip().lower()
        if answer in choices:
            return answer
        print("Invalid choice. Try again.")


def show_inventory(inventory):
    print("\n--- INVENTORY ---")
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print("- " + item)
    print("-----------------")


def random_encounter(health, inventory):
    if random.randint(1, 3) == 1:
        print("\nA monster jumps out of the darkness!")

        if "Silver Knife" in inventory or "Iron Sword" in inventory:
            print("You defend yourself with your weapon!")
            if random.randint(1, 2) == 1:
                print("You defeat the monster!")
            else:
                health -= 10
                print("The monster scratches you. You lose 10 health.")
        else:
            health -= 15
            print("You have no weapon! You lose 15 health.")

    return health


def room1(inventory, health):
    print("\n=== ROOM 1: THE ABANDONED HOUSE ===")
    print("You wake up in an abandoned house during a storm.")
    print("The front door is locked. A staircase leads down.")

    print("1. Search the room")
    print("2. Go downstairs")
    print("3. Try the front door")

    choice = get_choice("Choose 1, 2, or 3: ", ["1", "2", "3"])

    if choice == "1":
        if "Old Key" not in inventory:
            inventory.append("Old Key")
            print("You find an Old Key beneath a broken chair!")
        else:
            print("You already searched the room.")
    elif choice == "2":
        return "room2", health
    else:
        print("The front door is locked. You need a key.")

    return "room1", health


def room2(inventory, health):
    print("\n=== ROOM 2: THE BASEMENT ===")
    print("Water drips from the ceiling. Something is breathing nearby.")

    print("1. Search the cabinet")
    print("2. Enter the dark tunnel")
    print("3. Return upstairs")

    choice = get_choice("Choose 1, 2, or 3: ", ["1", "2", "3"])

    if choice == "1":
        if "Silver Knife" not in inventory:
            inventory.append("Silver Knife")
            print("You find a Silver Knife!")
        else:
            print("The cabinet is empty.")
    elif choice == "2":
        health = random_encounter(health, inventory)
        return "room3", health
    else:
        return "room1", health

    return "room2", health


def room3(inventory, health):
    print("\n=== ROOM 3: THE WHISPERING TUNNEL ===")
    print("Strange symbols cover the walls.")
    print("A locked gate blocks your path.")

    if "Old Key" in inventory:
        print("Your Old Key opens the gate!")
        return "room4", health

    print("You need an Old Key to open the gate.")
    print("1. Search the tunnel")
    print("2. Return to the basement")

    choice = get_choice("Choose 1 or 2: ", ["1", "2"])

    if choice == "1":
        health -= 5
        print("A symbol burns your hand! You lose 5 health.")
    else:
        return "room2", health

    return "room3", health


def room4(inventory, health):
    print("\n=== ROOM 4: THE DEAD FOREST ===")
    print("Dead trees surround you. Red eyes watch from the branches.")
    print("You see a cabin and a path leading to a ruined castle.")

    print("1. Search the forest")
    print("2. Enter the cabin")
    print("3. Walk toward the castle")

    choice = get_choice("Choose 1, 2, or 3: ", ["1", "2", "3"])

    if choice == "1":
        if "Healing Potion" not in inventory:
            inventory.append("Healing Potion")
            print("You find a Healing Potion!")
        else:
            print("You find only dead leaves.")
    elif choice == "2":
        return "room5", health
    else:
        return "room6", health

    return "room4", health


def room5(inventory, health):
    print("\n=== ROOM 5: THE ABANDONED CABIN ===")
    print("A message on the wall says:")
    print("'I have cities but no houses, forests but no trees,")
    print("and water but no fish. What am I?'")

    print("1. Answer the riddle")
    print("2. Search the cabin")
    print("3. Leave the cabin")

    choice = get_choice("Choose 1, 2, or 3: ", ["1", "2", "3"])

    if choice == "1":
        answer = input("Your answer: ").strip().lower()

        if answer in ["map", "a map"]:
            print("Correct! A hidden drawer opens.")
            if "Castle Key" not in inventory:
                inventory.append("Castle Key")
                print("You find the Castle Key!")
            else:
                print("The drawer is empty.")
        else:
            health -= 15
            print("Wrong! Poisonous gas fills the cabin.")
            print("You lose 15 health.")
    elif choice == "2":
        if "Healing Potion" not in inventory:
            inventory.append("Healing Potion")
            print("You discover a Healing Potion beneath the bed.")
        else:
            print("You find nothing else.")
    else:
        return "room4", health

    return "room5", health


def room6(inventory, health):
    print("\n=== ROOM 6: THE RUINED CASTLE ===")
    print("A huge monster guards the entrance.")
    print("A heavy door stands behind it.")

    if "Castle Key" in inventory:
        print("You use the Castle Key to open the door!")
        return "room7", health

    print("The door is locked. You need the Castle Key.")
    print("1. Fight the monster")
    print("2. Sneak away")
    print("3. Return to the forest")

    choice = get_choice("Choose 1, 2, or 3: ", ["1", "2", "3"])

    if choice == "1":
        if "Silver Knife" in inventory or "Iron Sword" in inventory:
            print("You attack the monster!")
            if random.randint(1, 2) == 1:
                print("You defeat the monster!")
                if "Monster Fang" not in inventory:
                    inventory.append("Monster Fang")
            else:
                health -= 20
                print("The monster injures you. You lose 20 health.")
        else:
            health -= 30
            print("You have no weapon! You lose 30 health.")
    elif choice == "2":
        print("You escape behind a broken wall.")
        return "room4", health
    else:
        return "room4", health

    return "room6", health


def room7(inventory, health):
    print("\n=== ROOM 7: THE FINAL CHAMBER ===")
    print("The Shadow King rises from a black throne!")
    print("'You will never leave this place alive!'")

    print("1. Fight the Shadow King")
    print("2. Use a Healing Potion")
    print("3. Escape through a side passage")

    choice = get_choice("Choose 1, 2, or 3: ", ["1", "2", "3"])

    if choice == "1":
        if "Iron Sword" in inventory:
            print("You attack with your Iron Sword!")
            if random.randint(1, 3) != 1:
                print("You defeat the Shadow King!")
                return "win", health
            else:
                health -= 25
                print("Dark magic hits you. You lose 25 health.")
        elif "Silver Knife" in inventory:
            print("You attack with your Silver Knife!")
            if random.randint(1, 2) == 1:
                print("You find the Shadow King's weakness and defeat him!")
                return "win", health
            else:
                health -= 30
                print("The Shadow King attacks! You lose 30 health.")
        else:
            health -= 35
            print("You have no weapon! You lose 35 health.")

    elif choice == "2":
        if "Healing Potion" in inventory:
            inventory.remove("Healing Potion")
            health = min(100, health + 30)
            print("You recover 30 health. Current health:", health)
        else:
            print("You don't have a Healing Potion!")
    else:
        if "Monster Fang" in inventory:
            print("The Monster Fang glows and opens the side passage!")
            print("You escape the castle alive!")
            return "win", health
        else:
            health -= 10
            print("The passage collapses! You lose 10 health.")

    return "room7", health


def start_game():
    wins, losses = load_game_stats()

    print("\n========================================")
    print("     THE CURSE OF THE SHADOW KING")
    print("========================================")
    print("Explore the haunted house and try to survive.")
    print("You start with 100 health.")

    inventory = []
    health = 100
    current_room = "room1"

    while health > 0 and current_room not in ["win", "lose"]:
        print("\nHealth:", health, "/ 100")
        print("1. Continue exploring")
        print("2. Check inventory")
        print("3. View game statistics")
        print("4. Quit game")

        action = get_choice("Choose an action: ", ["1", "2", "3", "4"])

        if action == "2":
            show_inventory(inventory)
            continue

        elif action == "3":
            print("\nTotal wins:", wins)
            print("Total losses:", losses)
            continue

        elif action == "4":
            print("You quit the adventure.")
            return

        if current_room == "room1":
            current_room, health = room1(inventory, health)
        elif current_room == "room2":
            current_room, health = room2(inventory, health)
        elif current_room == "room3":
            current_room, health = room3(inventory, health)
        elif current_room == "room4":
            current_room, health = room4(inventory, health)
        elif current_room == "room5":
            current_room, health = room5(inventory, health)
        elif current_room == "room6":
            current_room, health = room6(inventory, health)
        elif current_room == "room7":
            current_room, health = room7(inventory, health)

        if health <= 0:
            current_room = "lose"

    if current_room == "win":
        wins += 1
        print("\nYOU SURVIVED!")
        print("The Shadow King's curse is broken.")
    elif current_room == "lose":
        losses += 1
        print("\nGAME OVER.")
        print("The darkness has claimed another victim.")

    save_game_stats(wins, losses)

    print("\n=== FINAL RESULTS ===")
    print("Health remaining:", max(0, health))
    print("Items collected:", len(inventory))
    print("Total wins:", wins)
    print("Total losses:", losses)
    print("Your statistics have been saved.")


if __name__ == "__main__":
    start_game()



if __name__ == "__main__":
    start_game()
