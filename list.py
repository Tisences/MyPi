mates = ['ABC','def',"XyZ"]
print(mates)
print(len(mates))
print(mates[0])
print(mates[-1])

mates.append('BBB')
print(mates[-1])

mates.insert(1,'OOO')
print(mates)

print(mates.pop(1))
print(mates)

mates[1]=[1,2,3]
print(mates[1][2])