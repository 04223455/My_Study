class Student:
    name = None
    age = None
    address = None
    def __init__(self):
        self.name = input("请输入学生姓名:")
        self.age = input("请输入学生年龄:")
        self.address = input("请输入学生地址:")

for i in range(1,11):
    print(f"当前录入第{i}位学生信息,总共需要录入10位学生信息")
    stu = Student()
    print(f"学生{i}信息录入完成，信息为:【学生姓名：{stu.name},年龄{stu.age},地址:{stu.address}】")