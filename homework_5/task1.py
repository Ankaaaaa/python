with open('textfile_1.txt', 'tw', encoding='utf-8') as f:
    while True:
        my_input = input('введите строку или нажмите enter для выхода ')
        if not my_input:
            print("Finished")
            break
        else:
            f.writelines(my_input + '\n')
