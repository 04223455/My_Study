mystr = "itheima itcast boxuegu"
num1 = mystr.count("it")
mystr2 = mystr.replace(" ","|")
list1 = mystr2.split("|")
print(f"字符串itheima itcast boxuegu中有:{num1}个it字符")
print(f"字符串itheima itcast boxuegu,被替换空格后，结果：{mystr2}")
print(f"字符串itheima itcast boxuegu,按照|分隔后，得到：{list1}")