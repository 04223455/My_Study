num = int(10)
if int(input("请输入第一次猜想的数字：")) == num:
    print("你猜对啦！")
elif int(input("不对，再猜一次：")) == num:
    print("你猜对啦！")
elif int(input("不对，再猜最后一次：")) == num:
    print("你猜对啦！") 
else:
    print("Sorry,全部猜错啦，我想的是：%d" % num)