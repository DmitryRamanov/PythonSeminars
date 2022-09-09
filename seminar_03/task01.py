fname = input('Введите название файла: ')
f = open(fname,'w')
while True:
    s = input('Введите новую строку:')
    if s == '':
        break
    f.write(s + '\n')
f.close