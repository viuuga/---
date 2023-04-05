

def map_list(func, *args):
    mass = []
    for i in args:
        res = list(map(func, i ))
        mass.append(res)


    return mass


a, b, c, g = [1,2,3,4], [23,-1], [None, [25]], [23, 34, 33, 55]
print(map_list(str , a, b, c, g))
