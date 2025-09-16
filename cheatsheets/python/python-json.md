# Python JSON Cheatsheet

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