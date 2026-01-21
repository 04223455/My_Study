def str_reverse(s):
    print(f"字符串反转后是：{s[::-1]}")

def substr(s,x,y):
    return s[x:y]

if __name__ == '__main__':
    str_reverse("黑马程序员")
    print(substr("黑马程序员",1,3))