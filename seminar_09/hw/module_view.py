def print_message(text):
    print(text)

def tg_print_records(data):
    result = f'ТАБЛИЦА ТЕЛЕФОНОВ:\n'
    result += f'= ' * 35
    nm = 1
    for i in data:
        result += str(nm)+f'. '+i[0].ljust(14)+i[1].ljust(12)+i[2].ljust(14)+i[3].ljust(14)+i[4].ljust(7)+'\n'
        nm += 1
    result += f'= ' * 35
    return result

def print_records(data):
    print('ТАБЛИЦА ТЕЛЕФОНОВ: ')
    print('=' * 102)
    nm = 1
    for i in data:
        print(nm, '|', i[0].ljust(20), '|', i[1].ljust(20), '|', i[2].ljust(20), '|', i[3].ljust(15), '|', i[4].ljust(10), '|')
        nm += 1
    print('=' * 102)

def get_data(task):
    return input(task)

def show_menu():
    print('МЕНЮ')
    print('1 -> Поиск в справочнике')
    print('2 -> Добавить новую запись')
    print('3 -> Редактировать указанную запись')
    print('4 -> Удалить указанную запись')
    print('5 -> Сохранить изменения в справочник')
    print('6 -> Экспортировать данные в формате json')
    print('0 -> Выход из программы: ')
    return input("Выберите пункт в меню: ")

def tg_show_menu() -> str:
    return f'МЕНЮ\n1 -> Поиск в справочнике(/menu1)\n2 -> Добавить новую запись(/menu2)\n3 -> Редактировать указанную запись(/menu3)\n4 -> Удалить указанную запись(/menu4)\n5 -> Сохранить изменения в справочник(/menu5)\nВыберите пункт в меню(/menu*): '

'''
модель данных:
фамилия(50),имя(50),отчество(50),телефон(15),тип_телефона(раб/дом/личн)(4)
[
    ['фамилия','имя','отчество','телефон','тип_телефона']
    ,['фамилия','имя','отчество','телефон','тип_телефона']
    ,['фамилия','имя','отчество','телефон','тип_телефона']
    ......
]
'''

def add_new_record():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    telefon_number = input('Введите номер телефона: ')
    telefon_type = input('Введите тип телефоного номера (раб/дом/личн): ')
    return [surname, name, patronymic, telefon_number, telefon_type]

def edit_record(record_for_edit):
    surname = input(f'Введите новую фамилию вместо "{record_for_edit[0]}" или нажмите Enter, что бы пропустить: ')
    name = input(f'Введите новое имя вместо "{record_for_edit[1]}" или нажмите Enter, что бы пропустить: ')
    patronymic = input(f'Введите новое отчество вместо "{record_for_edit[2]}" или нажмите Enter, что бы пропустить: ')
    telefon_number = input(f'Введите новый номер телефона вместо "{record_for_edit[3]}" или нажмите Enter, что бы пропустить: ')
    telefon_type = input(f'Введите новый тип телефоного номера (раб/дом/личн) вместо "{record_for_edit[4]}" или нажмите Enter, что бы пропустить: ')
    if surname == '':
        surname = record_for_edit[0].strip()
    if name == '':
        name = record_for_edit[1].strip()
    if patronymic == '':
        patronymic = record_for_edit[2].strip()
    if telefon_number == '':
        telefon_number = record_for_edit[3].strip()
    if telefon_type == '':
        telefon_type = record_for_edit[4].strip()
    return [surname, name, patronymic, telefon_number, telefon_type]