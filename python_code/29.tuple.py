t1 = ('周杰伦',11,['football','music'])
index = t1.index(11)
print(index)
name = t1[0]
print(name)
del t1[2][0]
print(t1)
t1[2].append('coding')
print(t1)