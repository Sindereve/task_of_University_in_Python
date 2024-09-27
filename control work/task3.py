import re

value_input = input()

pattern = r"\bА"
r = re.sub(pattern=pattern,repl='аа',string=value_input)

pattern = r"\bр"
p_value = re.findall(pattern, string=r)

print(f'{r}\n{len(p_value)}')