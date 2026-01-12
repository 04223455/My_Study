print("欢迎来到黑马动物园。")
height = int(input("请输入你的身高（cm）："))
vip_level = int(input("请输入您的VIP级别："))
day = int(input("请告诉我今天几号："))
if height < 120:
    print("您的身高未超出120cm，可以免费游玩。")
elif vip_level > 3:
    print("您的VIP级别 > 3,可以免费游玩。")
elif day == 1:
    print("今天是1号，您可以免费游玩。")
# else:
#     print("您需要购票10元")
print("祝您游玩愉快。")