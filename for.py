# names = ['A','b','C','d']
# for name in names:
#     print(name)

# sum = 0
# num = list(range(1, 101))
# for x in num:
#     sum = sum+x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum = sum+n
#     n = n-2
# print(sum)
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print('Hello, %s!'%name)
sum = 0
n = 0
while n < 100:
    n = n+1
    if n % 2 == 0:
        continue
    sum = sum+n
print(sum)
