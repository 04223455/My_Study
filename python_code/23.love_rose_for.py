i = 1
for i in range(1,101):
    print(f"今天是向小美表白的第{i}天")
    for x in range (10):
        print("送你一朵玫瑰花")
    print("小美，我喜欢你")
print("今天是第%d天,表白成功了"% i)

i = 0 
for i in range(1,11):
    print(f"今天是表白第{i}天，加油")
    j = 1
    while j <= 10:
        print(f"这是送的第{j}朵玫瑰")
        j += 1
    print("小美，我喜欢你")
print(f"今天是表白的第{i}天，我成功了")

i = 1
while i <= 10:
    print(f"今天是表白第{i}天，加油")
    for j in range(1,11):
        print(f"这是送的第{j}朵玫瑰")
    print("小美，我喜欢你")
    i += 1
print(f"今天是表白的第{i-1}天，我成功了")