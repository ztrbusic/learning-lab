def collatz(number):
	if number % 2 == 0:
		number = number // 2
		print(number)
		return(number)
	else:
		number = 3 * number + 1
		print(number)
		return(number)

while True:
	try:
		number = int(input())
		break
	except ValueError:
		print("You must input a number")
		continue

while number != 1:
	number = collatz(number)