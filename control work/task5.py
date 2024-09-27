import re

pattern = r" \b0\b"

r = re.split(pattern=pattern,string=input())

size = len(r)
if r[size-1] == r[size-2]:
    print('0')
else:
    values = r[size-2].split()
    sum = 0
    for value in values:
        sum += int(value)
    print(sum)
    
