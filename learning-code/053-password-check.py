import re

def strong_pass_check(password):
	if not isinstance (password, str):
		return "Its not string"
	if len(password) < 8:
		return "Min 8 characters"
	if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", password):
		return "Wrong password"

password = input()
result = strong_pass_check(password)
print(result)