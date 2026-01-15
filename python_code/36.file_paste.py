f = open("D:/实验室/My_Study/我的学习笔记/bill.txt.txt","r",encoding = "UTF_8")
f1 = open("D:/实验室/My_Study/我的学习笔记/bill.txt.bak","w",encoding = "UTF_8")
for line in f:
    line = line.strip()
    list = line.split(",")
    if list[4] == "测试":
        continue
    f1.write(line)
    f1.write("\n")
f.close
f1.close