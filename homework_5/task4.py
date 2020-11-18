with open('textfile_4.txt', 'r', encoding='utf-8') as f:
    my_list = []
    for line in f:
        i = (line.split())
        my_list.append(i)
    print(my_list)
    for ind in my_list:
        if ind[0] == 'One':
            ind[0] = 'Один'
        if ind[0] == 'Two':
            ind[0] = 'Два'
        if ind[0] == 'Three':
            ind[0] = 'Три'
        if ind[0] == 'Four':
            ind[0] = 'Четыре'
    print(my_list)
    out_f = open('textfile_4_rus.txt', 'w')
    for i in my_list:
        for j in i:
            out_f.write(j + ' ')
        out_f.write('\n')
    out_f.close()