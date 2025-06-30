def shortest_word(y):
	if y == []:
		return ""
	else:
		shortest_word = y[0]
		for x in range(1, len(y)):
			if len(y[x]) <= len(shortest_word):
				shortest_word = y[x]
		return(shortest_word)

nested_list = ["banana", "to", "icecream", "Melita", "Željko", "Ana"]
print(shortest_word(nested_list))