import time, sys
from colorama import init, Fore, Style

def slow_print(text, delay):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(delay)
	print()

slow_print("""
	This is a simple RPG game.
	You are a fierce warrior entering a dungeon.
	You goal is to make simple choices to get to the end where you will have
	three questions to answer.
	If you answer the questions correctly, you will find out the meaning of life.
	""", 0.05)

player = {"name": "", "health": 100, "damage": 10}
enemy_troll = {"name": "Dungeon Troll", "health": 50, "damage": 5}
room_1 = {"description": "This is the first room. A troll lingers inside", "visited": False}

slow_print("Input player name: ", 0.03)
player["name"] = input()
slow_print("These are your stats:", 0.03)
print(player)

while True:
	slow_print("Press " + Fore.BLACK + "any key " + Style.RESET_ALL + "to continue to the first room: ", 0.05)
	for attempt in range(4):
		if attempt == 1:
			slow_print("C'mon, this is a pun older than... I don't know... you!?", 0.05)
			slow_print("Press " + Fore.BLACK + "any key " + Style.RESET_ALL + "to continue to the first room: ", 0.05)
		elif attempt == 2:
			slow_print("This is your last chance, for real!", 0.05)
		elif attempt == 3:
			slow_print("Goodbye!", 1)
			sys.exit()
		user_input = input()
		if user_input == "any key":
			break
	break
	
slow_print(room_1["description"], 0.05)
slow_print("This is the enemy and his stats:", 0.05)
print(enemy_troll)
