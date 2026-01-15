f = open("D:/实验室/My_Study/我的学习笔记/word.txt.txt","r",encoding = "UTF-8")
content = f.read()
num = content.count("itheima")
print(content)
print(num)

num = 0
for line in f:
    line = line.strip()
    content1 = line.split(" ")
    for word in content1:
        if word == "itheima":
            num += 1
print(num)