import random
num = random.randint(1,100)
i = 0
flag = True
while flag:
    guess_num = int(input("请输入你的猜想："))
    i += 1
    if guess_num == num:
        print("你第%d次就猜中了！"% i)
        flag = False
    elif guess_num > num:
        print("你猜的数大了")
    else :
        print("你猜的数小了")


        


