def display_inventory(inventory):
	print("Inventory: ")
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + " " + k)
		item_total += v
	print("Total number of items: " + str(item_total))

def add_to_inventory(inventory, added_items):
	for i in added_items:
		inventory.setdefault(i, 0)
		inventory[i] += 1
	return inventory

inv = {"arrows": 2, "swords": 5, "shields": 30}
print(inv)
add1 = ["gold coin", "dagger", "gold coin", "cape", "gold coin", "ruby"]
inv = add_to_inventory(inv, add1)
display_inventory(inv)