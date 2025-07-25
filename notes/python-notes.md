# Python Learning Notes
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

## 2025-07-03
**Dictionaries and making a library program**
- `a = input()` and `shelves[a] = []` - creates a new shelf
- `shelves[shelf_choice].append(new_book)` - adds a new book to the chosen shelf
- `print(shelves.keys())` - always use `()` when printing keys

## 2025-07-04
**Library program - cont'd**
- `input()` always returns string - can't compare with `== 1`

## 2025-07-08
**Library program - cont'd**
- **JSON** - JavaScript Object Notation
- write to file:
	```python
	with open("filename", "w", encoding="utf-8") as f:
		json.dump(dictname, f, ensure_ascii=False, indent=2)
	```
	- `with open` -  creates context manager, automatically closes files
	- `"w"` - opens file in write mode
	- `as f` - gives file temporary name "f" inside this block
	- `json.dump` - takes object (dict, list etc.) and writes it to file f
- save to file:
	```python
	try:
		with open("filename", "r", encoding="utf-8") as f:
			return json.load(f)
	except FileNotFoundError:
		return {}
	```

## 2025-07-09
- `return` - exits the whole function
- `break` - exits just the `while True` loop and function continues

**Automate the Boring Stuff - cont'd - Manipulating Strings**
- escape characters - `\'`, `\"`, `\t`, `\n`, `\\`
- raw string - `print(r"That is Carol\'s cat.")`
	- useful for file paths
- multiline strings - `"""` or `'''`
	- all quotes, tabs or newlines are considered a part of the string
	- used for comments that span multiple lines
- strings are indexed and can be sliced
- `in` and `not` can be used (case sensitive)
	```python
	"Hello" in "Hello word"
	True
	```
- **string interpolation** - `%s`
	- str() - doesn't need to be called
	`"My name is %s. I am %s years old." % (name, age)`
- **f-strings** - `f""`
	- `f"My name is {name}. I am {age} years old."`
	- if _int_ it can be modified - `{age + 1}`
- `.upper()` and `.lower()`
	- `variable.upper()`
	- do not change string inside variable unless - `variable = variable.upper()`
	- useful for normalizing inputs (`if input.lower()`)
- `.isupper()` and `.islower()` return Boolean
	- all have to be lower or upper, just letters are checked
- `.isalpha()` - only letters
- `.isalnum()` - only letters and numbers
- `.isdecimal()` - only numbers
- `.isspace()` - only spaces, tabs, and newlines
- `.istitle()` - only words that begin with uppercase, followed by lowercase letters
- `.startswith()`, `.endswith()`
- `.join()` and `.split()`
	- can join a list of strings or split a string into a list
	- `", ".join(["cats", "rats", "bats"])`
	- `"My name is Simon".split()`
- `.partition()` - `"Hello world!".partition("w")` - `("Hello", "w", "orld!")`
	- returns a tuple of three substrings
	- only first occurence of `"w"`
	- if separator string not found returns one full string and two empty
- `.rjust()`, `.ljust()`, `.center()`
	- e.g. `"Hello".rjust(10)` - "Hello" is 5 characters - 5 spaces added to its left to make a string of 10 characters
	- e.g. `"Hello".rjust(20, ".")` - specifies a fill character
- `.strip()`, `.lstrip()`, `.rstrip()` - strips characters
- _Unicode code point_ - `ord("A")`
- **pyperclip** module - has `copy()` and `paste()`

## 2025-07-16
**Started RPG game program**
- used `sys.stdout` for printing text one character at a time
	- ```
	def slow_print(text, delay):
		for character in text:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(delay)
		print()
	```
	- `.write` - prints without newline
	- `.flush` - forces to show immediately (no buffering)
	- `time.delay` - add delay per character

## 2025-07-22
**RPG game continued**
 - adding color:
 	- `from colorama import init, Fore, Style`
 - making an executable:
 	- `pip install pyinstaller`
 	- `pyinstaller --onefile file.py`

 ## 2025-07-25
 **RPG game continues**
 - learned `textwrap.dedent` of multiline f-strings
 	- eg:
 	```
	 	print(textwrap.dedent(f"""
	 					Some text.
	 					"""))
 	```











































