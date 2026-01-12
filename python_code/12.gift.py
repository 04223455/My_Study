age = int(input("你的年龄是多少："))
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的入职时间是多少：")
        if int(input()) > 2:
            print("你可以领取礼物")
        elif int(input("你的级别是多少：")) > 3:
            print("你也可以领取礼物")
        else:
            print("你不能领取礼物")
    else:
        print("你还不能领取")
else:
    print("你不能领礼物")
    