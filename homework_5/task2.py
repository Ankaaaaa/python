with open('textfile_2.txt', 'r', encoding='utf-8') as f:
    f.tell()
    j = 0
    for line in f:
        print(f'{line} количество слов: {len(line.split())}')
        print('*' * 50)
        j += 1
    print('количество строк в файле: ', j)





