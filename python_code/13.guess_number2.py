import random
num = random.randint(1,10)
guess_num = int(input("请输入数字："))
if guess_num == num:
    print("恭喜你！猜对了！")
else:
    if guess_num > num:
        print("大了")
    else:
        print("小了")
guess_num = int(input("请再输入数字："))
if guess_num == num:
    print("恭喜你！第二次猜对了！")
else:
    if guess_num > num:
        print("大了")
    else:
        print("小了")
guess_num = int(input("请最后输入数字："))
if guess_num == num:
    print("恭喜你！第三次猜对了！")
else:
    print("没有猜中！")