def print_all (*args,  sep = ' ', end = '\n'):
    new_str = ''
    for arg in args:
        new_str += str(arg) + sep
    new_str = new_str.rstrip(sep) + end
    return  new_str

print(print_all(1, 2, 3, 4, sep = '****', end = '@'))
print(print_all(1, 2, 3, 4, 5, end = '!!!'))