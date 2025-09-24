import re

date_pattern = re.compile(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([12]\d{3})$")
date = input()
match = date_pattern.fullmatch(date)
day, month, year = match.groups()
day = int(day)
month = int(month)
year = int(year)
 
if month == 2:
	if day > 29:
		print("Invalid entry.")
	elif day == 29:
		if year % 4 != 0:
			print("The year you entered is not a leap year!")
		elif year % 100 == 0 and year % 400 != 0:
			print("The year you entered is not a leap year!")

if month in (4, 6, 9, 11):
	if day > 30:
		print("This is not a valid date!")
else:
	if day > 31:
		print("This is not a valid date!")


