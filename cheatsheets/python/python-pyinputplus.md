# Python PyInputPlus Cheatsheet

- `import pyinputplus as pyip`

- `inputStr()`
- `inputNum()`
- `inputDateTime()`
- `inputMenu()`
- `inputYesNo()`
- `inputCustom(SOME_FUNCTION)`

- `pyip.inputStr()` - arguments:
	- `prompt=" "`, `default`, `blank`, `timeout`, `limit`
	- `allowRegexes`, `blockRegexes`, `applyFunc`, `postValidateApplyFunc`, `allowlistRegexes`, `blocklistRegexes`
	- `allowRegexes=[(r"^0$, "Yes, it is zero")]`