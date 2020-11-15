from sys import argv
parametr = argv[1:]
if 'help' in parametr:
    print('введите через пробел\n 1.зарплата сотрудника в час\n 2.количество отработаных часов\n 3.премия')
if len(parametr) == 3:
    print(f'зарплата сотрудника за {parametr[1]} часов со ставкой {parametr[0]} в час и премией {parametr[2]} составит '
          f'{int(parametr[0])*int(parametr[1])+int(parametr[2])}')

