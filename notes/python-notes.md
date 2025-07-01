# Python Notes 1
## 2025-06-30
**Dictionaries**
- unordered except from v3.7:
	- they remember the insertion orders of key-value pairs
- `.keys()`, `.values()`, `.items()`
	- can be used in `for` loops
	- can be made into lists with e.g. `list(dictionary.keys())`
	- tuple unpacking with `for k, i in dictionary.items()`
	- `in dictionary` always checks for keys
- `.get()` - two arguments: key and fallback: `dictionary.get("eggs", 0)`
	- use when you just want to _read_
- `.setdefault()` - two args: key and value to set
	- use when you want to _set_ if missing
- PrettyPrint - `import pprint`, `pprint.pprint`, `pprint.pformat`
	- `pformat` - returns, can be stored in a variable
	- `pprint` - just outputs, returns `None`

## 2025-07-01
**Dictionaries - continued**
- `for k, v in dict.items():` - loops through key-value pairs
- `"cat" in spam` vs. `"cat" in spam.keys()` - no difference
- `"cat" in spam` vs. `"cat" in spam.values()` - checks for "cat" in values of dictionary named spam
- to change a value in dictionary: `some_dictionary[key] = value`

**General notes**
- `return True` or `return False` always exits the `for` loop even if it not done yet
- functions do not use global variables, they need to be set inside the function
- dictionaries are mutable and it is not needed to return something in functions because they are modified in place
	- except if you assing a new variable to function output, then the new variable will be `None`