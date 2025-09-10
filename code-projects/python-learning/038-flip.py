import random

flip_list = []



for _ in range(100):
	flip_list.append(random.choice(["H", "T"]))

current_streak = 1
streak_count = 0

for flip in range(1, len(flip_list)):
	if flip_list[flip] == flip_list[flip - 1]:
		current_streak += 1
	else:
		current_streak = 1
	if current_streak == 6:
		streak_count +=1

print(streak_count)
