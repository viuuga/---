def filter_list(num, *args):
    mass = []
    for i in args:
        res = [list(filter(num, i ))]
        mass.append(res)
    return mass


num =  lambda a: type(a) in (int, float)

a, b, c, g = [1,2,3,4], [23,-1], [None, [25]], [23, [34], 33, 55]
print(filter_list(num , a, b, c, g))