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
- `import pprint` - 