import random
my_list = []
for i in range(0, 15):
    number = random.randint(0, 100)
    my_list.insert(i, number)
print(my_list)

my_len = len(my_list)

for i in my_list:
    if my_list.count(i)>1:
        while i in my_list:
            my_list.remove(i)
        print(f'удален {i}')
print(my_list)
if my_len == len(my_list):
    print('повторений не было, нажмите run еще раз для генерации нового списка')