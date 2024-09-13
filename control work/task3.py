input_value = int(input())
sum = 1
new_value = sum

for n in range(1,input_value+1):
    new_value = new_value *1/n
    sum = sum + new_value
    

print(f'{sum:.6}')

