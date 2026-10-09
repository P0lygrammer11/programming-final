# AL, EG, JT , NS
# location : classroom 
# Branch condition checking if current_room is equal to "classroom":
current_room = "classroom"
#   Print room environment text:
#"You are in the Classroom. You wake up. It is after hours, the sun has set, and the classroom door is locked."
print("You are in the Classroom. You wake up. It is after hours, the sun has set, and the classroom door is locked.")
#"Sitting at the teacher's desk is a terrifying Teacher Alien."
print("Sitting at the teacher's desk is a terrifying Teacher Alien.")
#"She is completely blind, but her massive extraterrestrial ears can hear a pin drop."
print("She is completely blind, but her massive extraterrestrial ears can hear a pin drop.")
#   Print navigation instructions:
#"Available navigation: type 'go north' to leave the room and head to the Hallway."
#Print puzzle options:
#"Available actions: type 'solve' to attempt to steal the Master Key."
#   Call input validation system tracking option array: ['go north', 'solve']
option_a = input("(1) go north to the hallway   (2) attemp to steal keys")
#   If player chooses 'go north':
if option_a == "1":
#     - Set current_room variable to "hallway"
    current_room = "hallway"
#If player chooses 'solve':
elif option_a == "2":
#- Print: "First action: Getting out of your seat"
    print("your getting out of your seat slowely")
#- Print [Option A]: Slide out of your chair and crawl quietly under the row of desks.
#- Print [Option B]: Dash out of your seat as fast as you can.


#     - Call input validation tracking choices 'a' and 'b'


#     - If choice is 'b':


#       - Print: "Result: LOSE. Your shoes squeak loudly on the linoleum. The Alien Teacher instantly spins around and drags you to detention. (Restart Room 1)"


#     - If choice is 'a':


#       - Print: "Result: WIN. You move silently across the floor and reach the side of her desk."


#       - Print: "Choice 2: Snatching the Key"


#       - Print [Option A]: Carefully slide the key off the desk while she turns to grade papers.


#       - Print [Option B]: Dive across the top of the desk to grab it quickly.


#       - Call input validation tracking choices 'a' and 'b'


#       - If choice is 'b':


#         - Print: "Result: LOSE. You knock over a metal cup full of pencils. The loud clattering alerts the alien, and you are caught. (Restart Room 1)"


#       - If choice is 'a':


#         - Print: "Result: WIN. You snag the key without a sound."


#         - Add "Master Key" string literal into global inventory list array if not already present


#         - Increment global item interaction counter variable by 1


#         - Print: "Choice 3: Opening the Door"


#         - Print [Option A]: Slide the key into the lock slowly and twist it gently.


#         - Print [Option B]: Frantically jam the key in and slam the handle down.


#         - Call input validation tracking choices 'a' and 'b'


#         - If choice is 'b':


#           - Print: "Result: LOSE. The heavy metal lock rattles loudly. A tentacle wraps around your ankle before you can step outside. (Restart Room 1)"


#         - If choice is 'a':


#           - Print: "Result: WIN. The door clicks open silently. You slip out into the hallway."


#           - Set current_room variable to "hallway"

# --------------------------------------------------------------------------

#Room 2, AL
print("Room 2")
print("Location: The Hallway")
print("You step into the long hallway, but freedom is far away. Guarding the corridor are the dreaded Triple T Principals (Tuntung Tung Sahur). At first, there is only one principal pacing back and forth. But every few seconds, they mysteriously multiply, cloning themselves until the hallway is completely swarming with angry principals!")
choice = input("Your goal is to successfully navigate the expanding crowd and reach the safety of the IT room at the end of the hall. You have 3 options: 1) Avoiding the first Principal, 2) Dealing with the Clones, 3) Sprint to the final door (Choose 1, 2 or 3)  ").isnumeric

# --------------------------------------------------------------------------

while True:
    if choice == "1":
        print("")
    elif choice == "2":
        print("")
    elif choice == "3":
        print("")
    else : 
        print("You dont know how to follo instructions ?")
        
        

# Branch condition checking if current_room is equal to "hallway":


#   Print room environment text:


#     "You are in the long Hallway, but freedom is far away. Guarding the corridor are the dreaded Triple T Principals (Tuntung Tung Sahur)."


#     "At first, there is only one principal pacing back and forth. But every few seconds, they mysteriously multiply, cloning themselves until the hallway is completely swarming with angry principals!"


#   Print navigation instructions:


#     "Available navigation: type 'go south' to return to the Classroom, or 'move east' to enter the IT Room."


#   Print puzzle options:


#     "Available actions: type 'solve' to attempt to navigate the expanding crowd."


#   Call input validation system tracking option array: ['go south', 'move east', 'solve']


#   If player chooses 'go south':


#     - Set current_room variable to "classroom"


#   If player chooses 'move east':


#     - Set current_room variable to "it_room"


#   If player chooses 'solve':


#     - Print: "Choice 1: Avoiding the first Principal"


#     - Print [Option A]: Wait for the principal to turn his back, then sprint to the nearest set of school lockers to hide.


#     - Print [Option B]: Try to casually walk past him like you belong there.


#     - Call input validation tracking choices 'a' and 'b'


#     - If choice is 'b':


#       - Print: "Result: LOSE. He spots you instantly. 'No walking in the halls after hours!' You are dragged straight to detention. (Restart Room 2)"


#     - If choice is 'a':


#       - Print: "Result: WIN. You successfully duck inside a locker just as a second clone manifests out of thin air."


#       - Print: "Choice 2: Dealing with the Clones"
print("")

#       - Print [Option A]: Grab a heavy janitor's mop bucket and roll it down the hallway as a noisy distraction.


#       - Print [Option B]: Try to weave and dodge your way through the crowd of multiplying principals.


#       - Call input validation tracking choices 'a' and 'b'


#       - If choice is 'b':


#         - Print: "Result: LOSE. There are simply too many of them. You bump right into a principal clone and get caught. (Restart Room 2)"


#       - If choice is 'a':


#         - Print: "Result: WIN. The cluster of cloned principals chases after the rolling bucket, clearing a straight path for you."


#         - Add "Mop Bucket" string literal into global inventory list array if not already present


#         - Increment global item interaction counter variable by 1


#         - Print: "Choice 3: The Final Door Sprint"


#         - Print [Option A]: Dive headfirst into the open doorway of the IT Server Room and slam the door shut behind you.


#         - Print [Option B]: Try to slowly open the IT room door so you don't make noise.


#         - Call input validation tracking choices 'a' and 'b'


#         - If choice is 'b':


#           - Print: "Result: LOSE. Taking too long gives the multiplying horde enough time to surround you. Hand on the doorknob, you are caught. (Restart Room 2)"


#         - If choice is 'a':


#           - Print: "Result: WIN. You barricade the door just as a dozen principals slam against it. You are safe for now."


#           - Set current_room variable to "it_room"


# --------------------------------------------------------------------------


# LOCATION: IT_ROOM


# --------------------------------------------------------------------------


# Branch condition checking if current_room is equal to "it_room":


#   Print room environment text:


#     "You are trapped in the IT Room. Suddenly, the rows of computers begin to flicker wildly. The school servers have overheated and ripped open a dark portal to the Upside Down."


#     "Cold ash falls from the ceiling, thick vines creep across the floor, and a terrifying Demogorgon steps through the rift, clicking its jaws as it tracks your body heat."


#   Print navigation instructions:


#     "Available navigation: type 'move west' to go back to the Hallway, or 'go north' to slip into the Staff Lounge."


#   Print puzzle options:


#     "Available actions: type 'solve' to try to shut down the portal."


#   Call input validation system tracking option array: ['move west', 'go north', 'solve']


#   If player chooses 'move west':


#     - Set current_room variable to "hallway"


#   If player chooses 'go north':


#     - Set current_room variable to "staff_lounge"


#   If player chooses 'solve':


#     - Print: "Choice 1: Surviving the Entry"


#     - Print [Option A]: Drop to the floor and cover yourself with a thick, discarded thermal server blanket.


#     - Print [Option B]: Throw a computer keyboard at the monster to scare it off.


#     - Call input validation tracking choices 'a' and 'b'


#     - If choice is 'b':


#       - Print: "Result: LOSE. The keyboard bounces harmlessly off its hide. It charges and catches you. (Restart Room 3)"


#     - If choice is 'a':


#       - Print: "Result: WIN. The blanket masks your body heat. The Demogorgon sniffs the air but misses you."


#       - Add "Thermal Blanket" string literal into global inventory list array if not already present


#       - Increment global item interaction counter variable by 1


#       - Print: "Choice 2: Closing the Portal"


#       - Print [Option A]: Locate the main cooling system lever and pull it to freeze the server core.


#       - Print [Option B]: Try to chop through the thick portal vines using a stray screwdriver.


#       - Call input validation tracking choices 'a' and 'b'


#       - If choice is 'b':


#         - Print: "Result: LOSE. The vines lash out, grabbing your arms and dragging you into the portal. (Restart Room 3)"


#       - If choice is 'a':


#         - Print: "Result: WIN. Freezing air blasts through the room. The cold breaks the portal's energy, causing the rift to snap shut and trapping the monster on the other side."


#         - Set current_room variable to "staff_lounge"


# --------------------------------------------------------------------------


# LOCATION: STAFF_LOUNGE


# --------------------------------------------------------------------------


# Branch condition checking if current_room is equal to "staff_lounge":


#   Print room environment text:


#     "You are in the Staff Lounge, looking for a window to the outside. But the lounge has been transformed into a dark, creaky nightmare labyrinth."


#     "Standing in the center of the room is Granny Horror, holding a baseball bat. She is completely blind but has hyper-sensitive hearing, and she has littered the floor with hidden bear traps."


#   Print navigation instructions:


#     "Available navigation: type 'go south' to step back into the IT Room, or 'move east' to bypass into the Gym."


#   Print puzzle options:


#     "Available actions: type 'solve' to try to cross the creaky lounge to reach the gym vent."


#   Call input validation system tracking option array: ['go south', 'move east', 'solve']


#   If player chooses 'go south':


#     - Set current_room variable to "it_room"


#   If player chooses 'move east':


#     - Set current_room variable to "gym"


#   If player chooses 'solve':


#     - Print: "Choice 1: Navigating the floor"


#     - Print [Option A]: Drop to your hands and knees to feel around in the dark for bear traps.


#     - Print [Option B]: Walk normally but use the screen light from your phone to see.


#     - Call input validation tracking choices 'a' and 'b'


#     - If choice is 'b':


#       - Print: "Result: LOSE. You don't see a bear trap hidden under a rug. SNAP! You scream in pain, and Granny instantly catches you. (Restart Room 4)"


#     - If choice is 'a':


#       - Print: "Result: WIN. You safely bypass two rusty bear traps hidden under the carpet."


#       - Print: "Choice 2: Distracting Granny"


#       - Print [Option A]: Pick up a ceramic coffee mug from a table and toss it into the far corner of the room.


#       - Print [Option B]: Try to sneak right past her while she is facing away from you.


#       - Call input validation tracking choices 'a' and 'b'


#       - If choice is 'b':


#         - Print: "Result: LOSE. You step on a majorly creaky floorboard. Granny spins around instantly and hits you with the bat. (Restart Room 4)"


#       - If choice is 'a':


#         - Print: "Result: WIN. The mug shatters. Granny sprints toward the noise, leaving the exit vent completely unguarded."


#         - Add "Coffee Mug" string literal into global inventory list array if not already present


#         - Increment global item interaction counter variable by 1


#         - Set current_room variable to "gym"


# --------------------------------------------------------------------------


# LOCATION: GYM


# --------------------------------------------------------------------------


# Branch condition checking if current_room is equal to "gym":


#   Print room environment text:


#     "You land on the wooden floor of the School Gym. Suddenly, the entire environment shifts into a video game world."


#     "The basketball hoops turn into floating brick blocks, and a horde of angry Goombas starts marching across the court toward you. Up on the bleachers, the PE Teacher is firing giant, homing Bullet Bills straight at your position!"


#   Print navigation instructions:


#     "Available navigation: type 'move west' to climb back to the Staff Lounge, or 'go north' to burst out to the Courtyard."


#   Print puzzle options:


#     "Available actions: type 'solve' to try to survive the chaotic assault."


#   Call input validation system tracking option array: ['move west', 'go north', 'solve']


#   If player chooses 'move west':


#     - Set current_room variable to "staff_lounge"


#   If player chooses 'go north':


#     - Set current_room variable to "courtyard"


#   If player chooses 'solve':


#     - Print: "Choice 1: Defending against the Goombas"


#     - Print [Option A]: Jump up and punch a glowing floating ? block right above your head.


#     - Print [Option B]: Try to slide-tackle the row of incoming Goombas.


#     - Call input validation tracking choices 'a' and 'b'


#     - If choice is 'b':


#       - Print: "Result: LOSE. There are too many of them. They swarm you and drain your health. (Restart Room 5)"


#     - If choice is 'a':


#       - Print: "Result: WIN. A Super Mushroom pops out! You absorb it, double in size, and gain temporary invincibility, allowing you to stomp right through the Goombas."


#       - Add "Super Mushroom" string literal into global inventory list array if not already present


#       - Increment global item interaction counter variable by 1


#       - Print: "Choice 2: Evading the Bullet Bills"


#       - Print [Option A]: Use your giant Mushroom strength to pick up a heavy gymnastics mat and use it as a shield.


#       - Print [Option B]: Try to outrun the homing missile by zigzagging across the basketball court.


#       - Call input validation tracking choices 'a' and 'b'


#       - If choice is 'b':


#         - Print: "Result: LOSE. The Bullet Bill tracks your movement perfectly and blows you sky-high. (Restart Room 5)"


#       - If choice is 'a':


#         - Print: "Result: WIN. The Bullet Bill crashes into the mat and explodes safely, allowing you to charge the exit doors and smash them wide open."


#         - Set current_room variable to "courtyard"


# --------------------------------------------------------------------------


# LOCATION: COURTYARD (THE FINAL ESCAPE)


# --------------------------------------------------------------------------


# Branch condition checking if current_room is equal to "courtyard":


#   Print room environment text:


#     "You burst out of the gym into the fresh air of the school courtyard! Freedom is right across the lawn. However, the school gates are locked tight under a heavy security lockdown."


#     "Searchlights crisscross the grass, and the Alien Teacher from Room 1, the Triplet Principals, and Granny are all closing in on you."


#     "This is your ultimate Henry Stickman Final Mission. You must pick a gadget from your backpack to make your final escape. Two choices are hilarious failures, and only one leads to victory!"


#   Print navigation instructions:


#     "Note: You are surrounded at the school perimeter boundary! You cannot move back to internal rooms now."


#   Print gadget choices:


#     "[Option 1: The Teleporter]"


#     "[Option 2: The School Bus]"


#     "[Option 3: The Rocket Launcher]"


#   Call input validation system tracking number options '1', '2', and '3'


#   If choice is '1':


#     - Print: "Result: FAIL. The screen glitches out. You vanish into thin air and reappear directly inside a locked cage in the principal's office. Text reads: FAIL - Wrong coordinates! (Restart Courtyard)"


#   If choice is '2':


#     - Print: "Result: FAIL. You run over to a parked school bus and try to hotwire it to smash through the gates. You don't know how to wire a bus. Sparks fly, setting off the horn. The Alien Teacher instantly swoops down and snatches you. Text reads: FAIL - Should've taken driving lessons! (Restart Courtyard)"


#   If choice is '3':


#     - Print: "Result: MISSION COMPLETE! BOOM! The gate flies off its hinges. You sprint through the smoke into the neighborhood, leaving the glitched school behind forever. Text reads: ESCAPE SUCCESSFUL!"


#     - Set current_room variable to "finished"






















room = (input("You find yourslef infront of three doors which one do you chose to walk into door:"))
print("Room:3")

while True:
    if room == 1:
       print("You walk in seeing a endless hallway you imedeatly regret your desition. The door shuts you run to wondering why it closed."/n ""  
      if room == 2:
 












print 








