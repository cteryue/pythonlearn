import json
import random
import re
import threading
import time
from typing import Union


class intherit_Parent01:
#    name = None
#    age = 24

#    def __init__(self,name,age):
#        self.name = name
#        self.age = age

    def test01(self):
        print("父类01")

class intherit_Parent02:
#    sex = None
#    role = None

#    def __init__(self,sex,role):
#        self.sex = sex
#        self.role = role

    def test02(self):
        print("父类02")

# 多继承在有同名方法或者同名属性时，按照从左到右的顺序，左边优先级最高
class intherit_Child(intherit_Parent02,intherit_Parent01):
    permissions = None

    # 覆写父类方法
    def test01(self):
        # 调用父类方法
        intherit_Parent01.test01(self)
        # 调用父类方法
        super().test01()
        print("这是覆写后的父类01")

    # 覆写父类方法
    def test02(self):
        # 调用父类方法
        intherit_Parent02.test02(self)
        # 调用父类方法
        super().test02()
        print("这是覆写后的父类02")

    def test03(self):
        print("子类")

# intherit_Child().test01()
# intherit_Child().test02()
intherit_Child().test02()
intherit_Child().test03()
intherit_Child().test01()


"""
类型注解对变量的几种写法
"""
var_1 : int = 1
var_2 : bool = True
var_3 : str = "测试"

class Student:
    pass
stu : Student = Student()

my_list : list = [1,2,3,4]
my_tuple : tuple = (1,2,3,4)
my_dict : dict = {1:"测试"}

my_list1 : list[int] = [1,2,3,4]
my_tuple2 : tuple[int,str,bool] = (1,"ces",True)
my_dict3 : dict[int,str] = {1:"测试"}

var_4 = random.randint(1, 10)    # type: int
var_5 = json.loads('{"name" : "zhangsan"}')         # type: dict
def test():
    return 10
var_6 = test()    # type: int

"""
类型注解对方法的写法，只有提示作用不是强制限制类型
"""
def add(x: int , y : int) -> int:
    return x + y
# add()

"""
Union类型用来描述混合类型注解
"""

var_7 : list[Union[int,str]] = [1,2,"c","e"]
var_8 : dict[str,Union[int , str]] = {"s":1,"q":"z"}
def func(date : Union[int,str]) -> Union[int , str]:
    return int,str
# func()

"""
多态
"""
class AC:
    def A1(self):
        pass
    def A2(self):
        pass
    def A3(self):
        pass

class T_AC(AC):
    def A1(self):
        print("T1")
    def A2(self):
        print("T2")
    def A3(self):
        print("T3")

class S_AC(AC):
    def A1(self):
        print("S1")
    def A2(self):
        print("S2")
    def A3(self):
        print("S3")

def test(ac : AC):
    ac.A1()

t1 = T_AC()
s1 = S_AC()
test(t1)
test(s1)

"""
闭包：既可以依赖外部变量，又可以不修改全局变量，确保变量安全
"""

# def outer(logo):
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
# o1 = outer("$$")
# o1("测试")

# def outer(num1):
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#     return inner
#
# o1 = outer(100)
# o1(200)

def outer(num1 = 0):
    def atm(num2,b = True):
        nonlocal num1
        if b:
            num1 += num2
            print(num1)
        else:
            num1 -= num2
            print(num1)
    return atm
o1 = outer()
o1(100)
o1(200)
o1(50,False)


"""
装饰器
"""

def outer1(func):
    def inner():
        print("1")
        func()
        print("2")
    return inner

@outer1
def sleep():
    import random
    import time
    print("3")
    time.sleep(random.randint(1,2))

sleep()

# o2 = outer1(sleep)
# o2()
"""
单例模式
"""
class Singleton:
    pass

s1 = Singleton()

s2 = s1
s3 = s1
print(s2)
print(s3)

"""
工厂模式
"""
class person:
    pass

class a1(person):
    pass

class a2(person):
    pass

class a3(person):
    pass

class test:
    def test03(self,msg):
        if msg == "a":
            return a1()
        elif msg == "w":
            return a2()
        else:
            return a3()



print(test().test03("a"))
print(test().test03("w"))
print(test().test03("s"))


"""
多线程
"""

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    # 字典方式传参
    t1 = threading.Thread(target = sing,kwargs={"msg":321})
    # 元组方式传参
    t2 = threading.Thread(target = dance,args=("s1",))

t1.start()
t2.start()



