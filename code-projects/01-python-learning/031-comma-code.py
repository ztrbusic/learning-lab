spam = ["apples", "bananas", "tofu", "cats"]

def commaCode(y):
	result = ""
	if y == []:
		print("Your list is empty")
	else:
		for x in range(len(y)):
			item = y[x]
			if x == len(y)-1:
				result = result + "and " + item
			else:
				result = result + item + ", "
		
	print(result) 

commaCode(spam)