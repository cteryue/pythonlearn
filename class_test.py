"""
类外面叫函数，类里面叫成员方法

"""


class Student:
    name = None
    age = None
    sex = None

stu1 = Student()
stu1.name = "张三"
stu1.age = "23"
stu1.sex = "男"

print(stu1.name)
print(stu1.age)
print(stu1.sex)


class test01:
#    name = None
#    sex = None

    # 这是构造方法
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    # 这是str方法，自己决定输出什么东西
    def __str__(self):
        return f"测试{self.name}和{self.sex}"

    # 这是比较方法，支持大于、小于比较
    def __lt__(self, other):
        return self.age > other.age

    # 这是比较方法，支持大于等于、小于等于比较
    def __le__(self, other):
        return self.age >= other.age

    # 这是比较方法，支持等于比较
    def __eq__(self, other):
        return self.age == other.age

# self的作用等同于方法本身，成员方法必须要携带这个参数
    def ces(self):
        print("name")
    def ces01(self,msg):
        print(f"这是测试{msg}{self.name}")

t1 = test01("ct","男",11)
print(t1,type(t1))
print(str(t1),type(t1))
t1.ces()
t1.ces01("陈天")

t2 = test01("ce","无",12)
t3 = test01("cw","无",21)
print(t2 >= t3)
print(t2 <= t3)
print(t2 == t3)

class privatization_test():

    __test = 2

    def __t1(self):
        print(2)

    def test01(self):
        if self.__test == 1:
            print(1)
        else:
            self.__t1()
            print(3)

si = privatization_test()
si.test01()











