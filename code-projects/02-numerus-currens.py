import json
import pprint

def load_from_file():
	try:
		with open("library.json", "r", encoding="utf-8") as f:
			return json.load(f)
	except FileNotFoundError:
		return {}

shelves = load_from_file()

# Add new shelf
def add_shelf(shelves):
	while True:
		shelf_name = input("Enter shelf name:")
		if shelf_name in shelves:
			print("This shelf already exists!")
		else:
			shelves[shelf_name] = []
			save_to_file(shelves)
			break
	print(shelves)
	return shelves

# Add new book to shelf
def add_book(shelves):
	print("What shelf would you like to add a book to?")
	print(shelves.keys())
	shelf_choice = input()
	if shelf_choice not in shelves.keys():
		print("This shelf does not exist!")
	else:
		new_book = input()
		shelves[shelf_choice].append(new_book)
		save_to_file(shelves)
		print("Book added successfully!")

# List books in shelf
def list_books(shelves):
	print("Pick a shelf.")
	pprint.pprint(shelves.keys())
	shelf_pick = input()
	print(shelves[shelf_pick])

# Searching for book
def book_search(shelves):
	print("Write author or title keyword.")
	keyword = input()
	for k, v in shelves.items():
		if keyword in str(v):
			print(v)
			print("Found! The book is on shelf: " + str(k))
		else:
			print("The keyword was not found in the database.")

# Menu
def menu(choice):
	if choice == "1":
		add_shelf(shelves)
	if choice == "2":
		add_book(shelves)
	if choice == "3":
		list_books(shelves)
	if choice == "4":
		book_search(shelves)

def save_to_file(shelves):
	with open("library.json", "w", encoding="utf-8")as f:
		json.dump(shelves, f, ensure_ascii=False, indent=2)

print("What do you want to do?\n1 - Add new shelf\n2 - Add new book\n3 - List books in a shelf\n4 - Search for a book")

choice = input()
menu(choice)