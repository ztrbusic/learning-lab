def longest_number(l):
	if l == []:
		return (None, [])
	else:
		highest_number = l[0]
		highest_list = []
		for number in l:
			if number > highest_number:
				highest_number = number
		for number in l:
			if number == highest_number:
				highest_list.append(number)
		return (highest_number, highest_list)

numbers_list = [1, 2, 4, 6, 4, 7, 8, 9, 10, 3, 10, 7, 10]
print(longest_number(numbers_list))