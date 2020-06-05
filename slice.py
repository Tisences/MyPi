# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[:3])
# L=list(range(1,100,2))
# print(L[-10:])


def trim(s):
    if s[:1]==' ':
        s=trim(s[1:])
    if s[-1:]==' ':
        s=trim(s[:-1])
    return s