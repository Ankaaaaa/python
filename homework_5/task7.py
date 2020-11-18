import json
with open('textfile_7.txt', 'r', encoding='utf-8') as f:
    my_list = []
    new_my_list = []

    my_dict = {}
    my_dict_2 = {}
    salary = 0
    j = 0
    for line in f:
        i = (line.split())
        my_list.append(i)

    for i in my_list:
        profit = int(i[2])-int(i[3])
        key = i[0]
        vel = profit
        my_dict[str(key)] = [str(vel)]
        if vel > 0:
            salary = salary + vel
            j += 1
    average_profit = salary/j
    my_dict_2['average_profit'] = [str(average_profit)]
    new_my_list.append(my_dict)
    new_my_list.append(my_dict_2)

    print(my_list)
    print(new_my_list)

with open("my_file.json", "w") as write_f:
    json.dump(new_my_list, write_f)
