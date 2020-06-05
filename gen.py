
# L = [x*x for x in range(1, 11)]
# print(L)
# G = (x*x for x in range(1, 11))
# for x in G:
#     print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1
    return 'done'


for x in fib(6):
    print(x)
