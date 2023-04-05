def print_all (args = input('введите аргументы: '),  sep = str(input('Что поставить между ними: ')), end = str(input('Чем закончим?: '))):
    if sep == '':
        sep = ' '
    if end == '':
        end = '\\n'
    new_str = ''
    for arg in args:
        new_str += str(arg) + sep
    new_str = new_str.rstrip(sep) + end
    return  new_str

print(print_all())
