from collections.abc import Iterable
from collections.abc import Iterator


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for value in L[1:]:
            if min > value:
                min = value
            if max < value:
                max = value
        return (min, max)


print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('12345', Iterable))
print(isinstance([x for x in range(10)], Iterable))
print(isinstance(123, Iterable))

print(isinstance((x for x in range(10)), Iterator))
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('abc'), Iterator))
