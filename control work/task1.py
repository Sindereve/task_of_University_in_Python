import re

pattern = r"^[\+|\-|\d]\d*\.\d+$"

value_input = input()

value = re.findall(pattern, value_input)

if value:
    pattern = r"[\.|\+|\-]"
    value = re.split(pattern=pattern, string=value[0])
    for i in value:
        size = len(i)
        if size > 0:
            print(size)

