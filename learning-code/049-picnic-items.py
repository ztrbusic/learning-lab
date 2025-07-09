def print_picnic(items_dict, left_width, right_width):
	print("PICNIC ITEMS".center(left_width + right_width, "-"))
	for k, v in items_dict.items():
		print(k.ljust(left_width, ".") + str(v).rjust(right_width))

picnit_items = {"sandwitches": 4, "apples": 12, "cups": 4, "cookies": 8000}
print_picnic(picnit_items, 12, 1)
print_picnic(picnit_items, 20, 6)