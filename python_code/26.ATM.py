money = 5000000
name = input("请输入用户名：")
def main():
    print("----------主菜单------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM,请选择操作：")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
    choice = input("请输入您的选择：")
    return choice
def check_money(show_header):
    global money
    if show_header:
        print("-----------查询余额------------")
    print(f"{name},您好，您的余额剩余：{money}元") 

def check_in(number):
    global money
    money += number
    print("----------存款------------")
    print(f"{name},您好，您存款{number}元成功")
    check_money(0)
    return 

def check_out(number2):
    global money
    money -= number2
    print("----------取款------------")
    print(f"{name},您好，您取款{number2}元成功")
    check_money(0)
    return 

while 1:
    choice = int(main())
    if choice == 1:
        check_money(1)
    elif choice == 2:
        num_1 = int(input("请问您要存款多少元："))
        check_in(num_1)
    elif choice == 3:
        num_2 = int(input("请问您要取款多少元："))
        check_out(num_2)
    else:
        print("程序已退出")
        break