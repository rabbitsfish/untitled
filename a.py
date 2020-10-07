# s1 = 'ab'
# s2 = 'ab'
# print(s1 is s2)
# print('字符串: ', id(s1), id(s2))
# s1 = 'ab' + 'c'
# s2 = 'ab' + 'c'
# print(s1 is s2)
# print('字符串: ', id(s1), id(s2))
#
# i1 = -5
# i2 = -5
# print('int负数: ', id(i1), id(i2))
# i1 = -6
# i2 = -6
# print('int负数: ', id(i1), id(i2))
# import os
# import sys
# base_url = 'C:\\Users\\dongff\\PycharmProjects\\untitled\\test04\\50.py'
# print(os.path.split(base_url))
# import requests
# url_M7 = 'http://zhuoyan-3g.gionee.com/ssc/cfg/getConfigs?versionName=5.3.2.t&packageName=com.android.music&namespace=config&versionCode=2026532023&imei=61374BE70391D138C59679F7928FD8C9&brand=GIONEE&appid=20003&model=GIONEE%20M6'
# result = requests.get(url_M7)
# print(result.json()['data'])
# if 'testX4' in result.json()['data'].keys():
#     print('~~~~~~~~~~~~')
# else:
#     print('!!!!!!!!!!!!!!!!!')
# s = '08980899825'
# if s.endswith(('12', '24')):
#     print('~~~~~~~~~~~~~~~~~`')
#
# li = [lambda :x for x in range(10)]
# print(li)
# print(li.__len__())
# def fun1(z, x=1, y=2):
#     return x+y+z
# print(fun1(0))
# x = 0
# res = 'aaaa' if x>1 else 'bbbb'
# print(res)
# a = [1, 2, 3, 4]
# print(a[0:len(a):2])
from multiprocessing import Process, Queue
# import os, time, random
# def proc_write(q, urls):
#     print('Process(%s) is writing...' % os.getpid())
#     for url in urls:
#         q.put(url)
#         print('Put %s to queue...' % url)
#         time.sleep(random.random())
# def proc_read(q):
#     print('Process(%s) is reading...' % os.getpid())
# import requests
# url = 'https://www.v2ex.com/api/nodes/show.json?name=python'
# r = requests.get(url)
# print(r.text)

# nodes = [{'name_model': 'python'}, {'name_model': 'android'}, {'name_model': 'node.js'}]
# import json
# data = json.dumps(str(nodes))
# print(data)
# class A:
#     a = 'abc'
#     b = 'bcd'
#     def sum(self):
#         s = self.a + self.b
#         return s
#
# if __name__ == '__main__':
#     print(A().sum())

# class Tree(object):
#     def __init__(self,name):
#         self.name = name
#         self.cate = "plant"
#
#     def __getattribute__(self, res):
#         print("哈哈")
#         print(res)
#         return object.__getattribute__(self, res) + '哇咔咔'
# aa = Tree("大树")
# print(aa.name)

# a = '["api_key", "imei", "model", "city", "sdk", "from"]'
# data = {'imei': '61374BE70391D138C59679F7928FD8C9', 'model': 'M7', 'api_key': '9dac6633be895da152187b9c1a5c0042', 'city': '6291CF4CB91BA6A334E4E7420791F862', 'sdk':
# 'toutiao_SDK', 'from': 'cdsp', 'api_sign': '385429275e983f1bd96c287c0501f9c1'}
# import  requests
# result = requests.get('http://t-3g.gionee.com/api/switch_a/silence', params=data).json()
# print(result)
# import copy
# class Crow:
#     def __init__(self, age):
#         self.age = age
#
# li = []
# c1 = Crow(5)
# li.append(c1)
# for n in range(20):
#     li_new = copy.copy(li)
#     pro_crow = 0
#     death_crow = 0
#     for i in li:
#         i.age += 1
#         if i.age >= 5 and i.age <= 15:
#             li_new.append(Crow(0))
#             pro_crow += 1
#         elif i.age > 15:
#             li_new.remove(i)
#             death_crow += 1
#
#     li = li_new
#     print('第%d年，出生:%d, 死亡:%d' % (n, pro_crow, death_crow))
# for i in li:
#     print(i.age)
# print(li.__len__())
# a = 'abcd' + 'e'
# b = 'abcde'
# print(id(a))
# print(id(b))
# print( a is b)
# class Foo:
#     pass
#
# class Bar(object):
#     pass
#
# foo = Foo()
# bar = Bar()
# print(type(Foo))
# print(type(foo))
# print(type(Bar))
# # print(type(bar))
# try:
#     b = 1
#     a = 1/0
#
# except ZeroDivisionError:
#     print('except')
# a = 1 + 1
# print('a:', a)
# myturp = (1, 2, 3)
# i = iter(myturp)
# j = enumerate(myturp)
# print(j.__next__())
# print(i.__next__())
# print(j.__next__())
# print(j.__next__())
# print(i.__next__())
# print(j.__next__())
# print(i.__next__())
# print(i.__next__())
# myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# l = iter(myDict)
# print(next(l))
# for eachKey in l:
#     print(':', eachKey)
# class IT_QA:
#     def __init__(self):
#         self.x = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.x > 10:
#             raise StopIteration
#         else:
#             self.x = self.x + 1
#             return self.x
#
# for i in iter(IT_QA, 7):
#     print(i)
# f = open('logcat.txt', 'r', encoding='utf-8')
# lines = f.readlines()
# f.close()
# for line in lines:
#     print(line, end='')
# l = (lambda:x for x in range(3))
# l1 = [lambda:x for x in range(3)]
# for i in l:
#     print(i())
# for j in l1:
#     print(j())
# python 中的闭包

# n = 10 #定义全局作用域变量
#
#
# def fn(): #形成闭包
#     n = 100 #定义局部变量n
#
#     def inner():
#         nonlocal n
#         n += 1 #这里定义操作相同变量n无法调用上层作用中的变量，如果只读不写则可以正常访问
#                # python3 中新增nonlocal 关键字可以调用上层作用域中的变量
#         print(n)
#
#     inner()
#     return inner #返回内嵌函数的地址，从而形成闭包
#     #形成闭包的条件
#     #1、必须要有一个内嵌函数
#     #2、内嵌函数中要对自由变量的引用
#     #3、外部函数必须返回内嵌函数
#
#
# t = fn()
# t()
# t()
# print(n)
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))