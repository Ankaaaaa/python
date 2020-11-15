import random
my_list = []
for i in range(0, 15):
    number = random.randint(0, 100)
    my_list.insert(i, number)
print(my_list)

y = 1
m = 0
new_my_list = []

for i in my_list:
    if y < len(my_list):
        if my_list[y] > i:
            new_my_list.insert(m, my_list[y])
            y +=1
            m +=1
        else:
            y +=1
print(new_my_list)

