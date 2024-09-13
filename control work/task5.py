input_value = int(input())

for value in range(1,input_value+1):
    square = value**2
    if  square <= input_value:
        print(f'{square}')
    elif square > input_value:
        break

    