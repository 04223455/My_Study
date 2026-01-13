count = 0
for i in range(1,21):
    import random
    num = random.randint(1,20)
    if num < 5:
        print(f"员工{i}，绩效分{num},低于5,不发工资,下一位。")
    else:
        count += 1
        print(f"向员工{i}发放工资1000元,账户余额还剩余{10000-1000*count}")
    if count == 10:
        break
print("工资发完了，下个月领取吧")
