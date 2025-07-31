import time, sys, textwrap
from colorama import init, Fore, Style
init()

#Function for printing text slowly
def slow_print(text, delay):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(delay)
	print()

#Player and enemy stats
player = {"name": "", "health": 100, "damage": 10}
enemy_room_1 = {"name": "Dungeon Troll", "health": 50000, "damage": 1000}

# #Intro
# slow_print(Fore.MAGENTA + "Simple RPG" + Style.RESET_ALL, 0.2)
# slow_print(textwrap.dedent(f"""
# 			This is a simple RPG game.
# 			You are a fierce warrior entering a dungeon.
# 			Your goal is to make simple choices to get to the end.
# 			If you play your choices right, you will find out the meaning of {Fore.YELLOW}life{Style.RESET_ALL}.
# 			"""), 0.05)

# #Player initialization
# slow_print("Input player name: ", 0.05)
# player["name"] = input()
# slow_print("Hi " + player["name"] + ". These are your stats:", 0.05)
# slow_print(textwrap.dedent(f"""
# 			Name: {player['name']}
# 			Health: {player['health']}
# 			Damage: {player['damage']}
# 			"""), 0.05)

# #Entrance to the first room
# while True:
# 	slow_print("Type " + Fore.BLACK + "any key " + Style.RESET_ALL + "to continue to the first room: ", 0.05)
# 	for attempt in range(4):
# 		if attempt == 1:
# 			slow_print("C'mon, this is a pun older than... I don't know... you!?", 0.05)
# 			slow_print("Type " + Fore.BLACK + "any key " + Style.RESET_ALL + "to continue to the first room: ", 0.05)
# 		elif attempt == 2:
# 			slow_print("This is your last chance, for real!", 0.05)
# 		elif attempt == 3:
# 			slow_print("Goodbye!", 1)
# 			sys.exit()
# 		user_input = input()
# 		if user_input == "any key":
# 			break
# 	break

# #Room 1
# slow_print("This is the first room. A troll lingers inside", 0.05)
# time.sleep(2)
# slow_print("This is the enemy and his stats:", 0.05)
# slow_print(textwrap.dedent(f"""
# 			Enemy name: {enemy_room_1['name']}
# 			Enemy health: {enemy_room_1['health']}
# 			Enemy damage: {enemy_room_1['damage']}
# 			"""), 0.05)
# slow_print("Hmmmm... This enemy seems unbeatable. You have just started on your journey, it would be a shame to die so early.", 0.05)
# slow_print(textwrap.dedent("""
# 			You have two choices:
# 			1. Fight,
# 			2. Run.
# 			Which one will it be?
# 			"""), 0.05)
# choice_room_1 = input()
# if choice_room_1 == "1" or choice_room_1 == "1." or choice_room_1 == "Fight" or choice_room_1 == "1. Fight":
# 	enemy_room_1["health"] -= 10
# 	slow_print(textwrap.dedent(f"""
# 			You deal 10 damage to the enemy.
# 			{enemy_room_1['name']} has {enemy_room_1['health']} health left.
# 			Enemy turn. {enemy_room_1['name']} deals {enemy_room_1['damage']} damage to {player['name']} .

# 			You are dead.

# 			Game over.
# 			"""), 0.05)
# 	sys.exit()
# elif choice_room_1 == "2" or choice_room_1 == "2." or choice_room_1 == "Run" or choice_room_1 == "2. Run":
# 	slow_print(textwrap.dedent(f"""
# 			You decided to run. Good. Your decision was wise, the enemy was too difficult for you, {player['name']}.
# 			But, in your attempt to flee quickly, you have fallen into a basement...
# 			"""), 0.05)
# else:
# 	slow_print("Don't play games with me.", 0.05)
# 	sys.exit()

# #Room 2
# time.sleep(2)
# slow_print(textwrap.dedent("""
# 			'Huh!? Where am I?'... it's pitch dark (not particulary suprising for a basement), damp
# 			(also not suprising), and strangely slippery. Feels like something slimy is crawling up your legs...
# 			"""), 0.05)
# time.sleep(1)
# slow_print("You need to get out, and fast. There is a door but it is locked. You see a glowing keypad asking for a combination.", 0.05)
# time.sleep(1)
# slow_print("_ _ ", 0.2)
# slow_print(textwrap.dedent(f"""
# 			You need to think fast, what could the number combination be!?
# 			You remember the book you read just yesterday, sitting in front of a fire, not battling monsters and dugenons.
# 			{Fore.YELLOW}The Hitchhikers Guide to the Galaxy{Style.RESET_ALL}...
# 			"""), 0.05)
# for attempt in range(3):
# 	if attempt == 1:
# 		slow_print(textwrap.dedent("""
# 			Wrong!
# 			The slimy thing is starting to crawl further up, your sensitive parts are dangerously close.
# 			The display reads: 'You have one more try.'
# 			"""), 0.05)
# 	elif attempt == 2:
# 		slow_print(textwrap.dedent("""
# 			WRONG!
# 			You percieve the sliminess of what is actually a furry, brown substance clogging your mouth, eyes and ears.
# 			You suffocate.
# 			"""), 0.05)
# 		sys.exit()
# 	code_room_2 = input()
# 	if code_room_2 == "42":
# 		slow_print(textwrap.dedent("""
# 				You hear a soft click of the lock, the door opens blinding you with the light outside.
# 				This was never actually a basement...
# 				"""), 0.1)
# 		break

#Room 3
# slow_print("""
# 	         \   |   /         
#            .-*-.
#         ― (  ☀  ) ―
#            `-*-'
#          /   |   \

#                   .          .     .            .
#              .      .     /\     .    *  .   .
#                     .    /  \  *     .     .
#                 .       /    \     .
#                      __/      \__
#                ___/              \___
#           ___/                      \___
#       ___/                            \___
#  ____/                                  \____
# /____________________________________________\\
# """, 0.01)

slow_print(textwrap.dedent(f"""
            The view is perfect. A mountain covered in mist with the sun just barely peeking through the clouds.
            Behind, a shack. Our hero wonders how did he end up here. There is a path he follows to the river where he discovers
            something shiny at the bottom. Does he jump into the river to pick the item?
            {Fore.MAGENTA}(This feels vaguely familiar... Finding shiny items at the bottom of rivers, my precious...){Style.RESET_ALL}
            1. Yes
            2. No
            """), 0.05)
while True:
	choice_room_3 = input()
	if choice_room_3 == "1." or choice_room_3 == "1" or choice_room_3 == "Yes" or choice_room_3 == "1. Yes" or choice_room_3 == "1.Yes":
		slow_print("Our hero picks up what seems to be a small dagger. When he grips it, he immediately feels much stronger:", 0.05)
		player["health"] += 999900
		player["damage"] += 99990
		dagger = 1
		slow_print("Your new stats are:", 0.05)
		slow_print(textwrap.dedent(f"""
				Health: {player['health']}
				Damage: {player['damage']}
				"""), 0.05)
		break
	elif choice_room_3 == "2." or choice_room_3 == "2" or choice_room_3 == "No" or choice_room_3 == "2. No" or choice_room_3 == "2.No":
		slow_print("You decide to sit down by the river, look at the water, the birds, the grass. You are not interested in the shiny item.", 0.05)
		dagger = 0
		break
	else:
		slow_print("Please choose a valid option!", 0.05)

#Room 4
slow_print(textwrap.dedent("""
			Following the path from the river, you find yourself in a dense and dark forest, immediately, the troll from the beginning jumps in front of you!
			'AARGGGHHHHHH!' - says the troll.
			"""), 0.05)
if dagger == 1:
	slow_print(textwrap.dedent("""
			You immediately reach for your dagger. The troll notices the shiny object in your hand and stops. Do you attack the troll or try to avoid him and run?
			1. Attack
			2. Run
			"""), 0.05)
	while True:
		choice_room_4 = input()
		if choice_room_4 == "1." or choice_room_4 == "1" or choice_room_4 == "Attack" or choice_room_4 == "1. Attack" or choice_room_4 == "1.Attack":
			enemy_room_1["health"] -= player["damage"]
			slow_print(f"You deal {player['damage']} damage to {enemy_room_1['name']}. His health drops to: {enemy_room_1['health']}", 0.05)
			player["health"] -= enemy_room_1["damage"]
			slow_print(f"{enemy_room_1['name']} deals {enemy_room_1['damage']} damage to you. Your health drops to: {player['health']}", 0.05)
			slow_print(f"{Fore.MAGENTA}You win! The troll is dead. Congratulations!{Style.RESET_ALL}", 0.05)
			sys.exit()
		elif choice_room_4 == "2." or choice_room_4 == "2" or choice_room_4 == "Run" or choice_room_4 == "2. Run" or choice_room_4 == "1.Run":
			slow_print(textwrap.dedent("""
				You run. Dagger in hand. Unfortunately you trip on the roots, stumble, fall, and pierce yourself.
				You die, the leaves cover your remains. Nobody knows or remembers your resting place."""), 0.05)
			sys.exit()
		else:
			slow_print("Please input the correct value", 0.05)
else:
	slow_print(textwrap.dedent("""
			You remember how useful would now be to have that shiny object, possibly a weapon of some kind, that you left on the bottom of the river.
			Still, you have your fists and need to decide, to run or to attack the troll:
			1. Attack
			2. Run
			"""), 0.05)
	while True:
		choice_room_4 = input()
		if choice_room_4 == "1." or choice_room_4 == "1" or choice_room_4 == "Attack" or choice_room_4 == "1. Attack" or choice_room_4 == "1.Attack":
			enemy_room_1["health"] -= player["damage"]
			slow_print(f"You deal {player['damage']} damage to {enemy_room_1['name']}. His health drops to: {enemy_room_1['health']}", 0.05)
			player["health"] -= enemy_room_1["damage"]
			slow_print(f"{enemy_room_1['name']} deals {enemy_room_1['damage']} damage to you. Your health drops to: {player['health']}", 0.05)
			slow_print(f"You die. {enemy_room_1['name']} eats your remains. Game over.", 0.05)
			sys.exit()
		elif choice_room_4 == "2." or choice_room_4 == "2" or choice_room_4 == "Run" or choice_room_4 == "2. Run" or choice_room_4 == "1.Run":
			slow_print(textwrap.dedent(f"""
			You slowly back up from the {enemy_room_1['name']} and quietly leave the scene. You find youself in front of a big tree, probably the oldest tree in the forest. The tree speaks:
			'How are you my child? You made all the right choices in your journey and you will be rewarded.
			{Fore.YELLOW}Life has no meaning... The hardest thing to grasp is the silence, the stillness of thoughts that lead to nowhere and have no purpose.
			Make peace with that, and you will be content. Enjoy the passing of time, do nice things, and do not expect anything in return.
			Go now!{Style.RESET_ALL}'
			"""), 0.05)
			sys.exit()
		else:
			slow_print("Please input the correct value", 0.05)



















