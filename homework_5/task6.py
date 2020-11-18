import re
with open('textfile_6.txt', 'r', encoding='utf-8') as f:

    my_dict = {}
    my_sum = 0
    for line in f:
        key = re.findall(r'^\w+', line)
        vel = re.findall('(\d+)', line)
        for i in vel:
            my_sum = my_sum + int(i)
        my_dict[str(key)] = [str(my_sum)]
        my_sum = 0






    # print(my_list)
    print(my_dict)




