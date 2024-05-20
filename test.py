print('Hello world')
print('Hello world！')
"""

这是一个长文本注释
-标题一
-标题二

"""
# 这是一个短文本注释
print(123)
print(12.32)
print("这是字符串类型")

# 这是一个短文本注释
print("这是字符串类型")

ct = 123
ce = "陈天"
ca = list(ce)
print(type(ca))
print(ca)
print(ct)
print("姓名为：",ct)
q = 100 - 10
w = 10 - q
# 转换为1位小数
p = float(w)
print(type(p),p)
r = "这是测试"
t = type(r)
print(t)
print(q)
print(w)
e = type(q)
print(type(q))

test01 = int(12.222)
print(f"转换成int类型{type(test01)}值为{test01}")

"""
运算符的一些运用
a += 1 表示a = a + 1 简易运算符
"""
a = 0
a += 1
print(a)
a1 = 1
a1 -= 1
print(a1)
a2 = 2
a2 *= 1
print(a2)
a3 = 3
a3 /= 2
print(a3)
a4 = 4
a4 //= 3
print(a4)
"""
字符串的三种写法，包括：'',"",三引号
可以用不同种类的引号互相包括
也可以使用占位符“\”来展示引号
"""
print("\"测试\"")
print("""'测试'""")
print('"测试"')
"""
字符串格式化方式的一种写法 
三种写法：
字符串：%s
整数：%d
浮点数：%f 默认保留六位小数
其中%m.nf
m：表示浮点数、整数的宽度的，当m小于整体长度时忽略m的长度，当m大于整体长度时，左边增加多出部分的空格
n：表示精度计算，包含四舍五入
特点：
1、根据占位符的不同拼接
2、做精度控制
3、按照顺序去匹配
"""
test02 = 123
test04 = 123.44
test03 = 321
test05 = 321.22
print("字符串拼接测试%s" % test02)
print("字符串拼接测试:%s,第二个数字:%d" % (test02,test03))
print("字符串拼接测试:%10.1f,第二个数字:%.2f" % (test04,test05))
# print("字符串拼接测试" + test02)

"""
字符串格式化方式的另一种写法 
特点：
1、不限制格式
2、不做精度控制
f是简写实际表示为：f = format
"""

t01 = "文本"
t02 = 123
t03 = 123.11
print(f"这是:\"{t01}\",整数:{t02},小数:{t03}")


"""
可以不用变量格式化，直接使用表达式进行格式化，做到代码的简洁
表达式：具有明确结果的代码语句
"""
print("拼接表达式：%s" % (1+2))
print("拼接表达式：%s" % (type('测试')))
print(f"拼接表达式：{2+2}")

"""
练习题
"""
name = "网易"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7

print(f"公司{name},股票代码{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f,经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,(stock_price * stock_price_daily_growth_factor ** growth_days)))



"""
这是input(提示信息)语句的用法
获取键盘输入的内容
输入的内容为永远为字符串


print(input("这是提示语："))
num = input()
num1 = int(num)
print(type(num),type(num1))
"""
z1 = 30
z2 = 20
if z1 < z2:
    print(type(30 >= 20))
elif z1 == z2:
    print(2)
else:
    print("1")

if 1 + 1 == 2:
    print(2)
    if 2+2 != 4:
        print(4)
    else:
        print(3)
else:
    print(1)

"""
i = 0
sum = 0
while i < 100:
    i += 1
    sum += i
print(sum)

import random
num = random.randint(1,100)
a = True
while a :
    b = int(input())
    if b == num:
        print("答对了")
        a = False
    else:
        if b > num :
            print("大了")
        else:
            print("小了")
"""


i = 1
while i < 10 :
    print(i , end='')
    j = 1
    while j <= i:
        if j == i:
            # \t是不让输入换行
            print(f"{j} * {i} = {j*i}\t")
        else:
            # end=''是在输入后面加上空格
            print(f"{j} * {i} = {j*i}\t" , end='')
        j += 1
    i += 1


name = "陈天"
for x in name :
    print(x)

test = "itheima is a brand of itcast"
sum = 0
for x in test :
    if x == "a":
        sum += 1
print(sum)
"""
range语法：
1、range(num)取0到mun-1的数字序列，不包含mun本身
2、range(num1，mun2)取num1到mun2-1的数字序列，不包含mun2本身
3、range(num1，num2，step)取num1到mun2-1的数字序列，不包含mun2本身，step为步长，默认为1
假如range(1,10,3)则序列为[1,4,7]
"""
for x in range(4):
    print(x)
    if x == 3:
        continue

for x in range(1,10):
    print(x)
    if x == 3:
        continue

for x in range(1,10,3):
    print(x)
    if x == 3:
        continue
i = 0
x = 0
for x in range(1,100):
    if x % 2 == 0:
        i += 1
print(i)
print(x)

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i} * {j} = {i*j}\t", end='')
    print()

i = 0
for i in range(1,10):
    if i%2 ==0 :
        break
    else:
        print(i)

i = 20000
for x in range(1,21):
    import random
    g = random.randint(1,10)
    if i == 0:
        break
    else:
        if g < 5:
            continue
        else:
            i -= 1000
            print(f"员工{x}，绩效{a},发放1000元")

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(count)
    return i
    print("完事")
str1 = "qweqweqweqwe"
str2 = "qweqweqweqw32e"
str3 = "qweqweqwe4242424qwe"
my1 = my_len(str1)
print(my1)
my_len(str2)
my_len(str3)

def addition(t1,t2):
    print(f"计算{t1} * {t2} = {t1*t2}")
addition(2,3)

def amd():
    a = 1 + 1
    return a
print(amd())
print(type(amd()))

def t1(x,y):
    """
    这是个加法函数
    :param x: 第一个数
    :param y: 第二个数
    :return: 计算结果
    """
    c = x + y
    return c
t1(1,2)


# global用法：它是一个关键字，可以设置内部定义的变量为全局变量

g1 = 100
def gl():
    global g1
    g1 = 120
    print(g1)
gl()
print(g1)

nameall = ['张三','李四','王五','赵六']
print(nameall)
print(type(nameall))
name_all = ['张三',123,True]
print(name_all)
print(type(name_all))
nameall1 = [['ces','test'],[1,2,3]]
print(nameall1)
print(type(nameall1))
print(nameall1[0][-1])
print(nameall1[1][2])


list1 = ['张三','张三','李四','王五','赵六']
print(list1.index('李四'))
#print(list1.index('李四1'))
list1[3] = '老六'
print(list1)
for x in list1:
    print(x)


list2 = [1,2,3,4,5]
# 在数组中加入下标位置的数据，原下标数据往后移
list2.insert(2,'苦茶')
print(list2)
# 在列表后面添加一个元素，可以是数组或者其他数据结构
list2.append(['dadada','老七'])
list2.append('老八秘制小憨包')
# 在列表后面添加容器，把要加入的容器内容依次取出，添加到目标数组后面
list2.extend([11,22,33,44,55,66])
list2.extend(list1)
print(f"列表变为：{list2}")
# 删除指定下标数据
del list2[1]
# 在列表中拿出指定下标数据，和删除一样，但是能赋值给变量
l2 = list2.pop(2)
print(f"取出的值为：{l2}")
print(list2)

# 删除某元素在列表中的第一个匹配项
list2.remove('张三')
print(list2)

# 清空所有列表数据
list2.clear()
print(list2)

# 统计一个元素在列表中的数量
l3 = [1,2,3,4,5,6,1,1,1,2,2,2,3,3,3,4,4,4]
l3.count(1)
print(l3.count(2))

# 统计列表中数据数量
print(len(l3))

l4 = [21,25,21,23,22,20]
l4.append(31)
l4.extend([29,33,30])
print(l4[0])
print(l4[-1])
print(l4.index(31))

l5 = ['张三','张三','李四','王五','赵六']
i = 0
while i < len(l5):
    print(l5[i])
    i += 1

for j in l5:
    print(j)



"""
元组
特性：
1、元组与列表是性质一样，除了不可更改元组内容
2、支持多数据
3、支持不同类型数据
4、有序
5、可重复
6、不可修改
7、支持for循环和while循环
特殊情况：元组内如果有list，list里的数据是支持修改的

"""
t1 = ('老八',' 李叔同','富贵','燕子',1,False)
t2 = ()
t3 = tuple()
print(f"t1:{t1}，类型为：{type(t1)}")
print(t2)
print(t3)

t4 = ('元组')
t5 = ('元组',)
print(f"t1:{t4}，类型为：{type(t4)}")
print(f"t1:{t5}，类型为：{type(t5)}")

# 元组的支持取数据，写法和list一致
t6 = ((1,True,'ces'),(2,False,'qwr'))
print(t6[0][1])
print(t6[1][1])
print(t6[1][2])
# 查照元素在元组中的位置
print(t1.index('老八'))
# 统计元素在元组中出现的次数
print(t1.count(1))
# 统计元组长度
print(len(t1))

t7 = (1,2,3,['ces',True,1])
t7[3][0] = 'test'
print(t7)

#练习题
t0 = ('周杰伦',11,['football','music'])
print(t0.index(11))
print(t0[0])
del t0[2][0]
t0[2].append('coding')
print(t0)
print(t0[0][1])
"""
字符串是恒不变的，无论使用什么方法，只是新增了一个字符串，不是在原字符串中更改
1、字符串只能存字符串
2、长度任意
3、支持下标索引
4、允许重复字符串存在
5、不可修改
6、支持循环
"""
s1 = '   itheima and itcast'
print(s1[1])
print(s1.index('h'))
# 替换字符串中所有字符串1的内容，替换为字符串2，得到一个新字符串
# 语法为：字符串.replace(字符串1,字符串2)
s2 = s1.replace('and','end')
print(s2)
print(s1)

# 去掉字符串中指定字符串,并且把一个字符串分割为多个字符串组成的list
s3 = s1.split(' ')
print(f"去掉指定字符串{s3}")

# 去掉前后空格
s4 = s1.strip()
print(s4)

# 去掉前后指定字符串，按照单个字符去掉
s5 = s1.strip('it')
print(s5)

# 统计指定字符串出现次数
print(s1.count('it'))

# 统计字符串的长度
print(len(s1))

s1 = "itheima itcast boxuegu"
print(s1.count('it'))
s2 = s1.replace(' ','|')
print(s2)
s3 = s2.split("|")
print(s3)

s4 = s1[1:5:1]
print(s4)

my_list = [1,2,3,4,5,6,7]
m1 = my_list[1:4:1]
print(m1)
print(my_list)
m5 = my_list[3:1:-1]
print(m5)
print(my_list)

my_list1 = (1,2,3,4,5,6,7)
m2 = my_list1[:]
print(f"这是m2{m2}")
print(my_list1)
m6 = my_list1[::-2]
print(m6)
print(my_list1)

str1 = "123424124"
m3 = str1[::2]
print(m3)
print(str1)
m4 = str1[::-1]
print(m4)
print(str1)

# 练习题
str1 = "13213,来堡汉小制秘八老,吃爱吃爱"
str2 = str1[18:11:-1]
print(str2,type(str2))
print(str1)

str3 = str1[::-1]
str4 = str3[5:12:1]
print(str4)

str5 = str3.split(",")
str6 = str5[1]
print(str6.strip("来"))

"""
集合：
特点：
1、无序
2、不允许有重复
"""
my_set = {1,2,3,4,5}
# 往集合中添加元素
my_set.add(6)
print(my_set)

# 删除集合中指定元素
my_set.remove(2)
print(my_set)

# 随机从集合中取出一个元素
s = my_set.pop()
print(s)
print(my_set)

# 清空集合
my_set.clear()
print(my_set,type(my_set))

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

# 拿到set1中有但是set2中没有的集合，组成一个新的set，并且对原有集合不影响
set3 = set1.difference(set2)
print(set3)
print(set2)
print(set1)

# 删除set1中有set2交集的元素，set1会发生变化，set2不变
set1.difference_update(set2)
print(set2)
print(set1)

# 2个集合合并，自动去重，获得一个新的集合
set4 = set1.union(set2)
print(set4)

# 统计集合中元素的数量
print(len(set1))

# set无法使用while循环遍历，因为set是无序的，无法根据下标遍历
# 只支持for循环遍历
for i in set2:
    print(i)

# 练习题

my_list = ['zhangsan','lisi','wanwu','zhaoliu','lisuton','laoba',1,True,'laoba']
set0 = set()
for x in my_list:
    print(x)
    set0.add(x)
print(set0)


"""
字典：
特点：
1、key：value 键值对
2、不可重复，如有重复，后面的value覆盖前面的
3、不支持下标索引
4、key不可重复，value可以重复
5、支持容纳多个数据和不同类型数据
6、支持修改
7、只支持for循环，不支持while循环，原因：没有下标索引
"""
map1 = {
    1:'zhangsan',
    2:'lisi',
    3:'wangwu',
    4:'zhaoliu',
    5:'laoba'
}
map2 = {}
map3 = dict()

# 字典里面嵌套字典
map4 = {
    "张三":{
        "数学": 11,
        "英语": 22,
        "语文": 33
    },
    "李四":{
        "数学": 12,
        "英语": 13,
        "语文": 14
    },
    "王五":{
        "数学": 23,
        "英语": 24,
        "语文": 25
    }
}

# 取元素
print(map4["张三"]["数学"])

# 对字典里有的key的值赋值，理解为修改
map4["张三"] = 44
print(map4)

# 对字典里没有的key值进行添加，理解为加入元素
map4["老八"] = 123
print(map4)

# 删除KEY，并且删除value
del map4["老八"]
print(map4)

# 取出KEY对应的value的值，并且删除字典对应元素
t1 = map4.pop("张三")
print(t1)
print(map4)

# 取出字典所有的KEY值
keys1 = map4.keys()
print(keys1)

# 遍历字典：方法一
for key in keys1:
    print(map4[key])

# 遍历字典：方法二
for key in map4:
    print(map4[key])

# 获取字典长度
print(len(map4))

# 清空字典
map4.clear()
print(map4)

print(len(map4))

l1 = [1,2,7,8,5,6]
print(max(l1))
print(min(l1))

l2 = (1,2,3,4)
print(max(l2))
print(min(l2))

l3 = 'qwertyuiqw'
print(max(l3))
print(min(l3))

l4 = {1,2,3}
print(max(l4))
print(min(l4))
print(type(l4))

l5 = {1:2,2:3,5:4}
print(max(l5))
print(min(l5))

print(set(l1),type(set(l1)))
print(tuple(l1),type(tuple(l1)))
print(str(l1),type(str(l1)))
print(list(l1),type(list(l1)))

print(set(l2),type(set(l2)))
print(tuple(l2),type(tuple(l2)))
print(str(l2),type(str(l2)))
print(list(l2),type(list(l2)))

print(set(l3),type(set(l3)))
print(tuple(l3),type(tuple(l3)))
print(str(l3),type(str(l3)))
print(list(l3),type(list(l3)))

print(set(l4),type(set(l4)))
print(tuple(l4),type(tuple(l4)))
print(str(l4),type(str(l4)))
print(list(l4),type(list(l4)))

print(set(l5),type(set(l5)))
print(tuple(l5),type(tuple(l5)))
print(str(l5),type(str(l5)))
print(list(l5),type(list(l5)))

# 从小到大排序，排序结果变为列表，并且会把字典变为只有key的列表
print(sorted(l1))

# 从大到小排序，反向排序
print(sorted(l1,reverse = True))

def test1():
    return 1,True

x,y = test1()
print(x)
print(y)

# 指定参数，支持入参中默认数据，如果调用函数时没有输入数据，就会传入默认值，有则传入输入的数据，默认值必须在最后面
def test2(a,b,c = 1):
    print(f"x = {a},y = {b},z = {c}")

test2(1,2)
test2(a = "1",b = "2",c = "3")
test2(b = "1",a = "2",c = "3")

# 不定长参数*args，会以元组类型存储元素，数量随意
def test3(*args):
    print(args)
    return args

test3(1,2,3,4,5)

# 不定长参数**kwargs，会以字典类型存储元素，数量随意，只能传入key = value键值对类型
def test4(**kwargs):
    print(kwargs)
    return kwargs

test4(name = "zhangsan",age = "23")

# 函数是可以传入另一个函数作为参数的
def c1(c2):
    print("--")
    a1 = c2(1,2)
    # a1 = c2
    print(type(c2))
    print(a1,type(a1))

# 匿名函数只能使用一次，并且不支持换行
c1(lambda x,y:x + y)
def c2(i,j):
    print("++")
    return i + j

c1(c2)

# 打开一个文件，并且给他实例化一个对象
f = open("test.txt","r",encoding = "UTF-8")
print(f,type(f))

# 若不传入参数读取所有数据，若传入指定参数读取指定字节数量数据，读取后保留下标，保留的下标会到下次读取时作为开始下标
print(f.read(2))

# 读取一行数据，保留的下标会到下次读取时作为开始下标
print(f.readline())
# print(f.readline())

# 读取所有数据，存放在一个list中
# print(f.readlines())

# for循环读取一个文件
for line in open("test.txt","r",encoding = "UTF-8"):
    print(line)

# 关闭文件对象，若不关闭，则只要程序运行中就会一致占用，无法对文件进行删除和修改操作
f.close()

# 可以自动关闭文件对象
with open("test.txt","r",encoding = "UTF-8") as f1:
    print(f1.readline())
    print(f1.readline())

# 当文件不存在时，创建文件，当文件存在，则清空文件内容，重新覆写文件内容
f2 = open("test1.txt","w",encoding = "UTF-8")

# 写入文件
f2.write("买了否冷")

# 将内存的内容刷新到文件中
f2.flush()

# close内置了flush的功能
f2.close()

f1 = open("test.txt","r",encoding = "UTF-8")
print(f1.read())

f1.close()

# a模式是追加写入，会在原文本后面直接写入数据，不会有任何换行或者空格操作
# 若文件没有创建，则创建文件，否则追加，其他操作和w模式一致
f1 = open("test2.txt","a",encoding = "UTF-8")
# \n为换行符
f1.write("\n加入一些文本")

f1.close()

f1 = open("test2.txt","r",encoding = "UTF-8")
print(f1.read())

f1.close()



try:
    open("abc.txt", "r")
except:
    open("abc.txt","w",encoding = "UTF-8").write("有异常")
    print('错误')

try:
    # print(qwrt)
    1/0
except ZeroDivisionError as a:
    print("没有该名称")
    print(a)
#
# try:
#     print(dssa)
#     1/0
# except(NameError,ZeroDivisionError) as e:
#     print(e)

try:
    print(dssa)
    1/0
except Exception as e:
    print(e)

try:
    print(a1)
    # 1/0
except Exception as e:
    print(e)
else:
    print("无异常")
finally:
    print("一直会执行的语句")

# import time

print("开始")
# time.sleep(1)
print("结束")

from time import sleep
# time.sleep(2)

from time import *
sleep(5)

# __all__ = ['tes']
def tes():
    print(111)

