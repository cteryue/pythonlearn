import m2
m2.a(1,2)


# from my_package import my_test01
# from my_package import my_test02
# my_test01.t1(2,3)
# my_test02.t2(3,1)

# from my_package.my_test02 import *
# from my_package.my_test01 import *
# t2(3,2)
# t1(1,1)

# from my_package.my_test01 import t1
# t1(5,4)

from my_package import *
my_test01.t1(2,3)

from inherit_test01 import s1
s2 = s1
s3 = s1
print(s2)
print(s3)