import re

def strong_pass_check(password):
	if not isinstance (password, str):
		return False
	if len(password) < 8:
		return False
		print("Min 8 characters")
	if re.search