mylist = [1,2,3,4,5,6,7,8,9,10]
listnew = []
index = 0
while index < len(mylist):
    element = mylist[index]
    if element % 2 == 0:
        if element != 0:
            listnew.append(element)
    index += 1
print(listnew)


mylist = [1,2,3,4,5,6,7,8,9,10]
listnew = []
for element in mylist:
    if element % 2 == 0:
        if element != 0:
            listnew.append(element)
print(listnew)