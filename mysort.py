l = sorted([2, -34, 1, -6, 4, -56, 23, 44], key=abs)
print(l)


def name(t):
    return -t[1]


l = sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)], key=name, reverse=False)
print(l)
