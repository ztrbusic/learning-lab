import re

def my_strip(string, chars=None):
	if chars is None:
		string = re.sub(r"^\s+", "", string)
		string = re.sub(r"\s+$", "", string)
	elif chars == "":
		return string
	else:
		pattern = f"[{re.escape(chars)}]"
		string = re.sub(f"^{pattern}+", "", string)
		string = re.sub(f"{pattern}+$", "", string)
	return string

string_out = input()
chars_out = input()
print(my_strip(string_out, chars_out))