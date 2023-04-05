def print_all (args = input('введите аргументы: '),  sep = str(input()), end = str(input())):
    if sep == '':
        sep = ' '
    if end == '':
        end = '\n'
    new_str = ''
    for arg in args:
        new_str += str(arg) + sep
    new_str = new_str.rstrip(sep) + end
    return  new_str

print(print_all())
