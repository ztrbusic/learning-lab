import time, sys
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
	slow_print("Press *any* key to continue to the first room: ", 0.05)
	user_input = input()
	if user_input == "any":
		break
	else:
		continue

slow_print(room_1["description"], 0.05)
slow_print("This is the enemy and his stats:", 0.05)
print(enemy_troll)
