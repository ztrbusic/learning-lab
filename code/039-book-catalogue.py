import pprint

shelves = {"Polica 1": "Mark Twain: Pustolovine Huckleberryja Finna"} 

# Add new shelf
# def add_shelf(shelves):
# 	shelf_name = input("Enter shelf name: ")
# 	if shelf_name not in shelves:
# 		shelves[shelf_name] = []
# 	else:
# 		print("This shelf already exists!")
# 	print(shelves)
# 	return shelves


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
		print("Book added successfully!")

add_book(shelves)
print(shelves)

# Searching for book

# Listing books in shelf

# 