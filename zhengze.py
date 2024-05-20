"""
正则表达式
"""
import re

s = "python test"
# 从第一个字符开始匹配，如果匹配不到则是None
r1 = re.match("python",s)
print(r1)
print(r1.group())
print(r1.span())

s1 = "1python test"
# 全局匹配，只匹配第一个匹配到的，如果匹配不到则是None
r2 = re.search("python",s1)
print(r2)
print(r2.group())
print(r2.span())


s2 = "1python test python"
# 全局匹配，匹配到所有的数据，返回一个list，如果没有就返回一个空的list
r3 = re.findall("python",s2)
print(r3)