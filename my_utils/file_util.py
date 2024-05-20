def print_file_info(file_name):
    try:
        f = open(file_name,"r",encoding = "UTF-8")
        return f.read()
    except:
        print("文件不存在")
    finally:
        f.close()

def append_to_file(file_name,data):
    try:
        f = open(file_name, "r", encoding="UTF-8")
    except:
        print("文件不存在")
    else:
        print("开始追加")
        f = open(file_name, "a", encoding="UTF-8")
        f.write("\n")
        f.write(data)
    finally:
        f.close()