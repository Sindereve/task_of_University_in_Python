import math



def f(sum, iter):
    new_sum = sum + (-1)**iter/(2*iter+1)**2
    return new_sum, sum

sum = 0.0
last_sum = 100
iter = 0

for i in range(3,7):
    while math.fabs(sum-last_sum) > 10**(-i):
        iter +=1
        sum, last_sum = f(sum, iter)

    print(f'Результат разницы = {math.fabs(sum-last_sum)} при {10**(-i)}')
    
    






