import re

def strip(string, chars=None):
	if chars == None:
		string = re.sub(r"^\s+", "", string)
		string = re.sub(r"\s+$", "", string)
	else:
		# nastaviti ovdje
	return string