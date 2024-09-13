input_value = int(input())
number_of_null = 0

while input_value > 0:
    digit = input_value%10
    if digit == 0:
        number_of_null+=1
    input_value = input_value//10
    
print(number_of_null)
