import random
numberOfStreaks = 0
for _ in range(10000):
	coinList =  []
	for _ in range(100):
		if random.randint(0, 1) == 0:
			coinList.append("T")
		else:
			coinList.append("H")
	count = 1
	for i in range(1, len(coinList)):
		if coinList[i] == coinList[i-1]:
			count += 1
		else:
			count = 1
		if count == 6:
			numberOfStreaks += 1
			break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))