def welcome(x):
    print("欢迎来到黑马程序员！请出示您的健康吗及72小时核酸证明,并配合测量体温")
    if x > 37.5:
        print(f"体温测量中，您的体温是{x}°C，需要隔离")
    else:
        print(f"体温测量中，您的体温是{x}°C，体温正常请进！")

welcome(38)

def add(x,y):
    result = x + y
    print(f"{x} + {y}的结果是{result}")

add(3,4)