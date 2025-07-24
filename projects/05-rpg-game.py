import time, sys
from colorama import init, Fore, Style

def slow_print(text, delay):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(delay)
	print()

slow_print(Fore.MAGENTA + "Simple RPG" + Style.RESET_ALL, 0.1)
slow_print("""
This is a simple RPG game.
You are a fierce warrior entering a dungeon.
You goal is to make simple choices to get to the end where you will have
three questions to answer.
If you answer the questions correctly, you will find out the meaning of life.
""", 0.1)

player = {"name": "", "health": 100, "damage": 10}
enemy_troll = {"name": "Dungeon Troll", "health": 50000, "damage": 1000}
room_1 = {"description": "This is the first room. A troll lingers inside", "visited": False}

slow_print("Input player name: ", 0.1)
player["name"] = input()
slow_print("Hi " + player["name"] + ". These are your stats:", 0.1)
slow_print(f"""
Name: {player['name']}
Health: {player['health']}
Damage: {player['damage']}
""", 0.1)

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
	
slow_print(room_1["description"], 0.1)
time.sleep(3)
slow_print("This is the enemy and his stats:", 0.1)
slow_print(f"""
Enemy name: {enemy_troll['name']}
Enemy health: {enemy_troll['health']}
Enemy damage: {enemy_troll['damage']}
""", 0.1)
