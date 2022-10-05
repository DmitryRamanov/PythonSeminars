from os import path
from csv import reader as csv_reader
from csv import writer as csv_writer
from json import dumps as js_dumps


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

def read_from_file(filename):
    records = []
    filename += '.csv'
    if path.exists(filename):
        with open(filename, 'r', newline="", encoding="utf-8") as fn:
            reader = csv_reader(fn)
            records = [i for i in reader]
    return records


def save_into_file(filename, data):
    filename += '.csv'
    with open(filename, 'w', newline="", encoding="utf-8") as fn:
        writer = csv_writer(fn)
        writer.writerows(data)


def export_to_jison(filename, data):
    filename += '.json'
    with open(filename, 'w', newline="", encoding="utf-8") as fn:
        fn.write(js_dumps(data, ensure_ascii=False, indent=4))