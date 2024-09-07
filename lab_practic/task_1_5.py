number = int(input())

sum_digits = 0
sqr = number**2

while number != 0:
    sum_digits += number % 10
    number //= 10


if (a:=sum_digits**3) == sqr:
    print(True)
    print(f'Куб суммы: {a} Квадрат числа:{sqr}')
else:
    print(False)
    print(f'Куб суммы: {a} Квадрат числа:{sqr}')