# Table Printer
def print_table(input_list):
	col_widths = [0] * len(input_list)
	for i in range(len(input_list)):
		for x in input_list[i]:
			col_widths[i] = max(len(x))

	print(col_widths)




table_data = [
	["apples", "oranges", "cherries", "banana"],
	["Alice", "Bob", "Carol", "David"],
	["blablablablablablabla", "cats", "moose", "goose"]
]

print_table(table_data)

