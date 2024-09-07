true_number_index = 0

for number in range(194441, 196501, 1):
    if number%100 == 93:
        for ind in range(2,number):
            if number%ind == 0:
                break
            elif ind == (number - 1):
                true_number_index+=1
                print(f'{true_number_index}) {number}')
