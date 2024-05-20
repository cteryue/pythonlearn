import json
my_dict = {
    "张三":1,
    "李四":2,
    "王五":3
}

# join.dumps函数将指定数据类型转换为json类型，其中ensure_ascii = False是将转换后的乱码转换为中文
data = json.dumps(my_dict,ensure_ascii=False)
print(data,type(data))

# join.loads函数将json类型转换为python类型，会自动识别转换后的类型，只能是列表或者字典
data = json.loads(data)
print(data,type(data))