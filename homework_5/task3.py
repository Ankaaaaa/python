with open('textfile_3.txt', 'r', encoding='utf-8') as f:
    my_list = []
    salary = []
    for line in f:
        i = (line.split())
        my_list.append(i)
    print(my_list)
    half_salary = 0
    j = 0
    for ind in my_list:
        if int(ind[1]) <= 20000:
            salary.append(ind[0])
        half_salary = half_salary + int(ind[1])
        j +=1
    print('сотрудники зарплата ниже 20000: ', salary)
    print('средняя зарплата: ', half_salary/j)

