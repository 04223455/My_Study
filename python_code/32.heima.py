mystr = "万过薪月,员序程马黑来,nohtyP学"
str1 = mystr[9:4:-1]
print(str1)

list1 = mystr.split(",")
str2 = list1[1]
str3 = str2.replace("来","")
str4 = str3[::-1]
print(str4)