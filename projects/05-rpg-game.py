import time, sys, textwrap
from colorama import init, Fore, Style

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

#Intro
slow_print(Fore.MAGENTA + "Simple RPG" + Style.RESET_ALL, 0.1)
slow_print(textwrap.dedent(f"""
			This is a simple RPG game. {time.sleep(3)}
			You are a fierce warrior entering a dungeon.
			Your goal is to make simple choices to get to the end
			where you will have three questions to answer.
			If you answer the questions correctly, you will find out the meaning of {Fore.YELLOW}life{Style.RESET_ALL}.
			"""), 0.05)

#Player initialization
slow_print("Input player name: ", 0.1)
player["name"] = input()
slow_print("Hi " + player["name"] + ". These are your stats:", 0.1)
slow_print(textwrap.dedent(f"""
			Name: {player['name']}
			Health: {player['health']}
			Damage: {player['damage']}
			"""), 0.05)

#Entrance to the first room
while True:
	slow_print("Press " + Fore.BLACK + "any key " + Style.RESET_ALL + "to continue to the first room: ", 0.1)
	for attempt in range(4):
		if attempt == 1:
			slow_print("C'mon, this is a pun older than... I don't know... you!?", 0.1)
			slow_print("Press " + Fore.BLACK + "any key " + Style.RESET_ALL + "to continue to the first room: ", 0.1)
		elif attempt == 2:
			slow_print("This is your last chance, for real!", 0.1)
		elif attempt == 3:
			slow_print("Goodbye!", 1)
			sys.exit()
		user_input = input()
		if user_input == "any key":
			break
	break

#Room 1
slow_print("This is the first room. A troll lingers inside", 0.1)
time.sleep(2)
slow_print("This is the enemy and his stats:", 0.1)
slow_print(textwrap.dedent(f"""
			Enemy name: {enemy_room_1['name']}
			Enemy health: {enemy_room_1['health']}
			Enemy damage: {enemy_room_1['damage']}
			"""), 0.05)
slow_print("Hmmmm... This enemy seems unbeatable. You have just started on your journey, it would be a shame to die so early.", 0.1)
slow_print(textwrap.dedent("""
			You have two choices:
			1. Fight,
			2. Run.
			Which one will it be?
			"""), 0.1)
choice_room_1 = input()
if choice_room_1 == "1" or choice_room_1 == "1." or choice_room_1 == "Fight" or choice_room_1 == "1. Fight":
	enemy_room_1["health"] -= 10
	slow_print(textwrap.dedent(f"""
			You deal 10 damage to the enemy.
			{enemy_room_1['name']} has {enemy_room_1['health']} health left.
			Enemy turn. {enemy_room_1['name']} deals {enemy_room_1['damage']} damage to {player['name']} .

			You are dead.

			Game over.
			"""), 0.1)
	sys.exit()
elif choice_room_1 == "2" or choice_room_1 == "2." or choice_room_1 == "Run" or choice_room_1 == "2. Run":
	slow_print(textwrap.dedent(f"""
			You decided to run. Good. Your decision was wise, the enemy was too difficult for you, {player['name']}.
			But, in your attempt to flee quickly, you have fallen into a basement...
			"""), 0.1)
else:
	slow_print("Don't play games with me.", 0.1)
	sys.exit()

#Room 2
time.sleep(2)
slow_print("""
			'Huh!? Where am I?'... it's pitch dark (not particulary suprising for a basement), damp
			(also not suprising), and strangely slippery. Feels like something slimy is crawling up your legs...  
			""", 0.1)
























