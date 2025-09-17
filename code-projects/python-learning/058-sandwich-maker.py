import pyinputplus as pyip

total_cost = 0

breads = {"wheat": 10, "white": 15, "sourdough": 30}
bread_type = pyip.inputMenu(list(breads.keys()), prompt="Choose a bread type:\n", numbered=True)
total_cost += breads[bread_type]

protein = {"chicken": 10, "turkey": 10, "ham": 5, "tofu": 15}
protein_type = pyip.inputMenu(list(protein.keys()), prompt="Choose a protein type:\n", numbered=True)
total_cost += protein[protein_type]

cheese_response = pyip.inputYesNo("Do you want cheese with that? ")
if cheese_response == "yes":
	cheese = {"cheddar": 20, "swiss": 10, "mozzarella": 10, "gouda": 5}
	cheese_type = pyip.inputMenu(list(cheese.keys()), prompt="Choose a cheese:\n", numbered=True)
	total_cost += cheese[cheese_type]

mayo_response = pyip.inputYesNo("Do you want mayo? ")
if mayo_response == "yes":
	total_cost += 5

mustard_response = pyip.inputYesNo("Do you want mustard? ")
if mustard_response == "yes":
	total_cost += 5

lettuce_response = pyip.inputYesNo("Do you want lettuce? ")
if lettuce_response == "yes":
	total_cost += 3

tomato_response = pyip.inputYesNo("Do you want tomato? ")
if tomato_response == "yes":
	total_cost += 3

quantity = pyip.inputInt("How many sandwiches do you want? ", min=1)
total_cost *= quantity

print(f"""
Thank you! Your sandwich is ready.
You need to pay {total_cost} EUR.
Have a nice day.
""")