from itertools import count, cycle

"""А"""

n = int(input('введите число с которого хотите сгенирировать список: '))
my_if = int(input('введите число которое будет последним элементов последовательности: '))
my_list = []
i = 0
for el in count(n):
    my_list.insert(i, el)
    i += 1
    if el > my_if-1:
        break
print(my_list)

"""Б"""

count = 0
for item in cycle('XYZ'):
    if count > 7:
        break
    print(item)
    count += 1
