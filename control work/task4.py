import re

value_input = input()

pattern = r"^#[ABCDEFabcdef|0-9]{6}$"
r = re.findall(pattern=pattern,string=value_input)
if r:
    print('Правильное выражение')