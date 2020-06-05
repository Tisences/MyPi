# L = list(range(1, 100, 2))
# print(L)
# L = [x*x for x in range(1, 11)if x % 2 == 0]
# print(L)
# L = [m+n for m in 'ABC' for n in 'xyz']
# print(L)
# delete file
import os
import shutil

dir = 'share/files'
L = [d for d in os.listdir(dir)]
for x in L:
    if x[:1] != '.':
        fileName = dir+"/"+x
        print(fileName)
        if os.path.isfile(fileName):
            os.remove(fileName)
        elif os.path.isdir(fileName):
            shutil.rmtree(fileName, True)
