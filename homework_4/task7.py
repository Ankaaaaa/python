from math import factorial

n = int(input('введите последний элемент последовательности от 1 до 100: '))


def fact(n):
    for el in range(1, n + 1):
        yield factorial(el)


i = 1
for el in fact(n):
    print(f'факториал {i} равен {el}')
    i += 1
