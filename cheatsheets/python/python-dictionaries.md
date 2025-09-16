# Python Dictionaries Cheatsheet

- `.keys()`, `.values()`, `.items()`
- `list(dictionary.keys())` - make a list out of dictionary
- `for k, i in dictionary.items()` - tuple unpacking
- `in dictionary` - always checks for keys
- `dictionary.get("eggs", 0)` - for reading, always two arguments

- **PrettyPrint**
	- `import pprint`, `pprint.pprint`, `pprint.pformat`
	- `pformat` - returns, can be stored in a variable
	- `pprint` - just outputs, returns `None`

- `for k, v in dict.items():` - loops thorugh key-value pairs
- `"cat" in spam` vs. `"cat" in spam.keys()` - no difference
- `"cat" in spam` vs. `"cat" in spam.values()` - checks for "cat" in values of dictionary named spam
- `some_dictionary[key] = value` - used to change a value in dictionary