def triangles():
    n = 0
    l = [1, ]
    while True:
        n = n+1
        if n == 1:
            pass
        # elif n == 2:
            # l = [1, 1]
        else:
            ll = []
            for m in range(n-2):
                ll.append(l[m]+l[m+1])
            l = [1]+ll+[1]
        yield l


def triangles1():
    L = [1, ]
    while True:
        yield L
        L = [1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
    # pass


n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for x in results:
    print(x)
