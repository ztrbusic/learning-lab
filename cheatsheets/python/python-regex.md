# Python Regex Cheatsheet

- `\d` - digit character
- `{x}` - do something _x_ times
- `import re` - all regex functions for Python
- `re.compile` - returns _Regex_ object
- `.search()` - searches the passed string for any matches
- `.group()` - extract matched text from a `.search()`
- `()` - make groups - `(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")`
- `.groups()` - returns a tuple with all groups
- `findall()` - finds all matched strings

- **Character Classes**
- `\d` - numeric digits from 0-9
- `\D` - any character that is _not_ a numeric digit 0-9
- `\w` - any letter, numeric digit, or underscore
- `\W` - any character that is _not_ a letter, numeric or underscore
- `\s` - any space, tab, or newline
- `\S` - any character that is _not_ a space, tab, or a newline
- `[a-zA-Z0-9]` - e.g. custom character class
- `[^aeiouAEIOU]` - negative character class
- `^` and `$` match the beggining or the end
- `.` - wildcard
- `.*` - match **everything** - uses greedy mode
- `re.DOTALL` - match also `\n` with `.*`
- `re.IGNORECASE` or `re.I` - ignores case, e.g. `(r"robocop", re.I)`
- `sub()` - substitutes found text
- `re.VERBOSE` - ignore whitespace and comments inside regex string
- `|` - _bitwise OR_ operator (pipe) - `re.IGNORECASE | re.DOTALL` etc.