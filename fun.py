import math
from functools import reduce

# def add(x, y, f):
#     return f(x) + f(y)
#
#
# print(add(2, 3, math.sqrt))

# def f(x):
#     return x * x
#
#
# r = map(f, range(1, 10))
# print(list(r))
#
# print(list(map(math.sqrt, range(1, 10))))
#
#
# def add(x, y):
#     return x + y
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# print(reduce(fn, [1, 2, 3, 4, 5, 6, 7]))

DIGTTS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def cha2num(s):
    return DIGTTS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(cha2num, s))


print(str2int('123'))


def normalize(name):
    # name = str(name)
    return name[:1].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(list(filter(lambda x: x % 2 == 1, range(1, 10))))


def prod(L):
    return reduce(lambda x, y: x * y, L)


def str2float(s):
    DIGTTS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    index = s.find('.')
    s1 = s[:index] + s[index + 1:]
    temp = reduce(lambda x, y: x * 10 + y, map(lambda x: DIGTTS[x], s1))
    return temp / (10 ** (len(s) - index - 1))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


f = lazy_sum(1, 2, 3, 5, 6, 3, 9)
print(f())
