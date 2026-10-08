# AL, EG , JT , NS


invintory = []
user_hp = 0


print("===================== W E L C O M E =========================")
print("==============E S C A P E _ N I G H T _ S C H O O L ============")
game_start = input("=============== T O   P L A Y  E N T E R (Y)============").capitalize()
if game_start == "Y":
    print("room loading.......")
else:
    return room_1
    
#NS
#room 1
while True(room_1):
    print("\n=== ROOM 1 ===")
#You wake up. It is after hours, the sun has set, and the classroom door is locked. Sitting at the teacher's desk is a terrifying Teacher Alien. She is completely blind, but her massive extraterrestrial ears can hear a pin drop. If you make too much noise, she will instantly snatch you and send you to permanent detention!
    print("You wake up. It is after hours, the sun has set, and the classroom door is locked. Sitting at the teacher's desk is a terrifying Teacher Alien. She is completely blind, but her massive extraterrestrial ears can hear a pin drop. If you make too much noise, she will instantly snatch you and send you to permanent detention!")
#Your goal is to sneak across the classroom, grab the Master Key off her desk, and unlock the exit door.
    option_a =input("Your goal is to sneak across the classroom, (1)grab the Master Key off her desk, and unlock the exit door or (2)Dash out of your seat as fast as you can. (chosse 1 or 2)").strip().lower()
    if not option_a.isnumeric():
        print("please eneter a number")
    else:
        if option_a == "1":
##Result: WIN. You move silently across the floor and reach the side of her desk.
            print(" You move silently across the floor and reach the side of her desk.")
#[Option B]: Dash out of your seat as fast as you can.
        elif option_a == "2":
            print("\n Your shoes squeak loudly on the linoleum. The Alien Teacher instantly spins around and drags you to detention.")
            print("Restarting Room 1...")
            continue
#Result: LOSE. Your shoes squeak loudly on the linoleum. The Alien Teacher instantly spins around and drags you to detention. (Restart Room 1)
#Choice 2: Snatching the Key
    print("\n#Choice 2: Snatching the Key")
    option_b = input("Do you: (1) Carefully slide the key off the desk, or (2) Dive across the top of the desk to grab it? ").strip()
#[Option A]: Carefully slide the key off the desk while she turns to grade papers.
    if option_b == "1":
#Result: WIN. You snag the key without a sound.
        print(" You snag the key without a sound.")
#[Option B]: Dive across the top of the desk to grab it quickly.
    if option_b == "2":
#Result: LOSE. You knock overa metal cup full of pencils. The loud clattering alerts the alien, and you are caught. (Restart Room 1)
        print("You knock overa metal cup full of pencils. The loud clattering alerts the alien, and you are caught")
#Choice 3: Opening the Door 
#[Option A]: Slide the key into the lock slowly and twist it gently.
#Result: WIN. The door clicks open silently. You slip out into the hallway.
#[Option B]: Frantically jam the key in and slam the handle down.
#Result: LOSE. The heavy metal lock rattles loudly. A tentacle wraps around your ankle before you can step outside. (Restart Room 1)

#AL, Room 2
while True :
    print("Room 2 The Hallway")
    print("You step into the long hallway, but freedom is far away. Guarding the corridor are the dreaded Triple T Principals (Tuntung Tung Sahur). At first, there is only one principal pacing back and forth. But every few seconds, they mysteriously multiply, cloning themselves until the hallway is completely swarming with angry principals!")
    optiona = input("Your goal is to successfully navigate the expanding crowd and reach the safety of the IT room at the end of the hall. You can 1) Avoid the first Principal, 2) Dealing with the Clones, 3) The Final Door Sprint (Choose 1,2, or 3)")
    if not options.isnumeric() :
        print("You dont know how to follow instructions ?")
    else:
        if options == "1":
            print("He spots you instantly. No walking in the halls after hours! You are dragged straight to detention.")
            print("Restarting Room 2")
            continue
        elif options == "2":
            
    
#Choice 1: Avoiding the first Principal
#[Option A]: Wait for the principal to turn his back, then sprint to the nearest set of school lockers to hide.
#[Option B]: Try to casually walk past him like you belong there. 
print("He spots you instantly. No walking in the halls after hours! You are dragged straight to detention.") #Result: LOSE. (Restart Room 2)
#Choice 2: Dealing with the Clones
#[Option A]: Grab a heavy janitor's mop bucket and roll it down the hallway as a noisy distraction.
print("The cluster of cloned principals chases after the rolling bucket, clearing a straight path for you") #Result: WIN.
#[Option B]: Try to weave and dodge your way through the crowd of multiplying principals.
print("There are simply too many of them. You bump right into a principal clone and get caught.") #Result: LOSE. (Restart Room 2)
#Choice 3: The Final Door Sprint
#[Option A]: Dive headfirst into the open doorway of the IT Server Room and slam the door shut behind you.
print("You barricade the door just as a dozen principals slam against it. You are safe for now.") #Result: WIN.
#[Option B]: Try to slowly open the IT room door so you don't make noise.
print("Taking too long gives the multiplying horde enough time to surround you. Hand on the doorknob, you are caught.") #Result: LOSE. (Restart Room 2)





#JT room 3
# Room 3: The IT Room (Theme: Stranger Things)
#You are trapped in the server room. Suddenly, the rows of computers begin to flicker wildly. The school servers have overheated and ripped open a dark portal to the Upside Down. Cold ash falls from the ceiling, thick vines creep across the floor, and a terrifying Demogorgon steps through the rift, clicking its jaws as it tracks your body heat.
print("You are trapped in the server room. Suddenly, the rows of computers begin to flicker wildly. The school servers have overheated and ripped open a dark portal to the Upside Down. Cold ash falls from the ceiling, thick vines creep across the floor, and a terrifying Demogorgon steps through the rift, clicking its jaws as it tracks your body heat.")
print("Your goal is to shut down the portal and escape before you become monster food.")
print (input("Do you A: Drop to the floor and cover yourself with a thick, discarded thermal server blanket or do you B: throw a computer keyboard at the monster to scare it off:")) .lower()
optionA = ()
optionB = ()
while True:
      if optionA == a:
        print("The blanket masks your body heat. The Demogorgon sniffs the air but misses you. You live")
    
        if optionA == b:
            print("The keyboard bounces harmlessly off its hide. It charges and catches you. You have died")
            print("Restart Room 3 choice 1")
            continue
        break
print(input("Closing the Portal do you want to A: Locate the main cooling system lever and pull it to freeze the server core. or do you want to B: Try to chop through the thick portal vines using a stray screwdriver:"))
while True:
    if optionB == a:
        print("Freezing air blasts through the room. The cold breaks the portal's energy, causing the rift to snap shut and trapping the monster on the other side. You survive")

    if optionB == b:
        print(" The vines lash out, grabbing your arms and dragging you into the portal. You died")   
        print("Restart room 3")     
            
 choice 2 
        continue   
        break
ice 1: Surviving the Entry
#[Option A]: Drop to the floor and cover yourself with a thick, discarded thermal server blanket.
#Result: WIN. The blanket masks your body heat. The Demogorgon sniffs the air but misses you.
#[Option B]: Throw a computer keyboard at the monster to scare it off.
#Result: LOSE. The keyboard bounces harmlessly off its hide. It charges and catches you. (Restart Room 3)
#Choice 2: Closing the Portal
#[Option A]: Locate the main cooling system lever and pull it to freeze the server core.
#Result: WIN. Freezing air blasts through the room. The cold breaks the portal's energy, causing the rift to snap shut and trapping the monster on the other side.
#[Option B]: Try to chop through the thick portal vines using a stray screwdriver.
#Result: LOSE. The vines lash out, grabbing your arms and dragging you into the portal. (Restart Room 3)


# Room 4: The Staff Lounge (Theme: Granny Horror)
#You stumble out of the freezing IT room and into the staff lounge, looking for a window to the outside. But the lounge has been transformed into a dark, creaky nightmare labyrinth. Standing in the center of the room is Granny Horror, holding a baseball bat. She is completely blind but has hyper-sensitive hearing, and she has littered the floor with hidden bear traps.
#Your goal is to cross the creaky lounge to reach the school gym vent without setting off a trap or making a sound.
#Choice 1: Navigating the floor
#[Option A]: Drop to your hands and knees to feel around in the dark for bear traps.
#Result: WIN. You safely bypass two rusty bear traps hidden under the carpet.
#[Option B]: Walk normally but use the screen light from your phone to see.
#Result: LOSE. You don't see a bear trap hidden under a rug. SNAP! You scream in pain, and Granny instantly catches you. (Restart Room 4)
#Choice 2: Distracting Granny
#[Option A]: Pick up a ceramic coffee mug from a table and toss it into the far corner of the room.
#Result: WIN. The mug shatters. Granny sprints toward the noise, leaving the exit vent completely unguarded.
#[Option B]: Try to sneak right past her while she is facing away from you.
#Result: LOSE. You step on a majorly creaky floorboard. Granny spins around instantly and hits you with the bat. (Restart Room 4)
while True:
    print("\n=== ROOM 4 ===")
    print("You stumble out of the freezing IT room and into the staff lounge, looking for a window to the outside. But the lounge has been transformed into a dark, creaky nightmare labyrinth. Standing in the center of the room is Granny Horror, holding a baseball bat. She is completely blind but has hyper-sensitive hearing, and she has littered the floor with hidden bear traps.")
    print("Your goal is to cross the creaky lounge to reach the school gym vent without setting off a trap or making a sound.")
    print("\n#Choice 1: Navigating the floor")
    option_c = input("Do you: (1) Drop to your hands and knees to feel around in the dark for bear traps, or (2) Walk normally but use the screen light from your phone to see? ").strip()
    if option_c == "1":
        print("You safely bypass two rusty bear traps hidden under the carpet.")
        break
    elif option_c == "2":
        print("You don't see a bear trap hidden under a rug. SNAP! You scream in pain, and Granny instantly catches you.")
        print("Restarting Room 4...")
        continue
#Room 5: The School Gym (Theme: Mario)
#You drop out of the vent and land on the wooden floor of the gym. Suddenly, the entire environment shifts into a video game world. The basketball hoops turn into floating brick blocks, and a horde of angry Goombas starts marching across the court toward you. Up on the bleachers, the PE Teacher is firing giant, homing Bullet Bills straight at your position!
#Your goal is to survive the chaotic assault and break through the heavy gym double-doors.
#Choice 1: Defending against the Goombas
#[Option A]: Jump up and punch a glowing floating ? block right above your head.
#Result: WIN. A Super Mushroom pops out! You absorb it, double in size, and gain temporary invincibility, allowing you to stomp right through the Goombas.
#[Option B]: Try to slide-tackle the row of incoming Goombas.
#Result: LOSE. There are too many of them. They swarm you and drain your health. (Restart Room 5)
#Choice 2: Evading the Bullet Bills
#[Option A]: Use your giant Mushroom strength to pick up a heavy gymnastics mat and use it as a shield.
#Result: WIN. The Bullet Bill crashes into the mat and explodes safely, allowing you to charge the exit doors and smash them wide open.
#[Option B]: Try to outrun the homing missile by zigzagging across the basketball court.
#Result: LOSE. The Bullet Bill tracks your movement perfectly and blows you sky-high. (Restart Room 5)

#The Final Escape: The Main Courtyard (Theme: Henry Stickman)
#You burst out of the gym into the fresh air of the school courtyard! Freedom is right across the lawn. However, the school gates are locked tight under a heavy security lockdown. Searchlights crisscross the grass, and the Alien Teacher from Room 1, the Triplet Principals, and Granny are all closing in on you.
#This is your ultimate Henry Stickman Final Mission. You must pick a gadget from your backpack to make your final escape. Two choices are hilarious failures, and only one leads to victory!
#The Final Choice: Pick Your Item
#[Option 1: The Teleporter]: You pull out a sci-fi teleporter gadget and press the button.
#Result: FAIL. The screen glitches out. You vanish into thin air and reappear directly inside a locked cage in the principal's office. Text reads: FAIL - Wrong coordinates! (Restart Courtyard)
#[Option 2: The School Bus]: You run over to a parked school bus and try to hotwire it to smash through the gates.
#Result: FAIL. You don't know how to wire a bus. Sparks fly, setting off the horn. The Alien Teacher instantly swoops down and snatches you. Text reads: FAIL - Should've taken driving lessons! (Restart Courtyard)
#[Option 3: The Rocket Launcher]: You pull out an absurdly oversized rocket launcher and aim it directly at the locked front gates.
#Result: MISSION COMPLETE! BOOM! The gate flies off its hinges. You sprint through the smoke into the neighborhood, leaving the glitched school behind forever. Text reads: ESCAPE SUCCESSFUL!



