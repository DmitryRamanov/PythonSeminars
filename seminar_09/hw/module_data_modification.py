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

def sort_data(data):
     data.sort(key=lambda x: x[0])

def delet_record(choice, data):
     if choice.isnumeric() and 0 <= int(choice) - 1 <= len(data) - 1:
          data.pop(int(choice) - 1)

def search_record(choice, data):
     if choice == '':
          result = data
     else:
          result = list(filter(lambda x: choice in x[0] or choice in x[1] or choice in x[2] or choice in x[3] or choice in x[4], data))
     return result

def add_new_record(new_record, data):
     data.append(new_record)

def get_record(choice, data):
     if choice.isnumeric() and 0 <= int(choice) - 1 <= len(data) - 1:
          return data[int(choice) - 1]
     else:
          return None