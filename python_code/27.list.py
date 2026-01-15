mylist = [21,25,21,23,22,20]
mylist.append(31)
mylist.extend([29,33,30])
num1 = mylist[0]
del mylist[-1]
num2 = mylist.index(31)
print(mylist)
print(num1,num2)