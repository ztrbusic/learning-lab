inventory = {}

def add_shelf(inventory):
	shelf_name = input("Write a new for your new shelf:")
	if shelf_name in inventory:
		print("Shelf name already exists.")
	else:
		inventory[shelf_name] = []
		print("Shelf " + shelf_name + " added.")

