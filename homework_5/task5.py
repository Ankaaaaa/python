with open('textfile_5.txt', 'w+', encoding='utf-8') as f:
    my_input = input('введите числа через пробел: ')
    f.writelines(my_input)
with open('textfile_5.txt', encoding='utf-8') as f_obj:
        my_list = f_obj
        my_str = my_list.readline()
        my_result = my_str.split()
        result = 0
        for el in my_result:
                result = result + int(el)
        print('сумма введеных чисел: ', result)

