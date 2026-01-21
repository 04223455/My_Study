def print_file_info(file_name):   
    f = None
    try:
        f = open(file_name,"r",encoding = "UTF-8")
        content = f.read()
        print(content)
    except Exception as e:
        print("文件不存在")
    finally:
        if f:
            f.close()

def append_to_file(file_name,data):
    f1 = open(file_name,"a",encoding = "UTF-8")
    f1.write(data)
    f1.write("\n")
    f1.close

