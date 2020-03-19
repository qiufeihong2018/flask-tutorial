# # 一元二次方程
# import math

# def quadratic(a,b,c):
#     x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
#     x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
#     return x1,x2

# print(quadratic(2,3,1))


# def add_end(L=[]):
#     L.append('end')
#     return L

# print(add_end())

# # def add_end(L=None):
# # ...     if L is None:
# # ...             L=[]
# # ...     L.append('end')
# # ...     return L
# # ...

# def calc(*numbers):
#     res=0
#     for num in numbers:
#         res=res+num*num
#     return res

# # print(calc([1,2,3]))
# # print(calc((1,2,3)))
# # 在参数前面加上*，numbers就会变成一个元组
# print(calc(1,2,3))

# def product(*numbers):
#     res=1
#     for num in numbers:
#         res=res*num
#     return res

# print(product(5))
# print(product(5,6))
# print(product(5,6))
# print(product(5,6,7,9))

# 利用递归函数移动汉诺塔
# def move(n,a,b,c):
#     if n==1:
#         print('move',a,'-->',c)
#     # elif n==2:
#     #     print(a,'-->',b)
#     #     print(a,'-->',c)
#     #     print(b,'-->',c)
#     # elif n==3:
#     #     print(a,'-->',c)
#     #     print(a,'-->',b)
#     #     print(c,'-->',b)
#     #     print(a,'-->',c)
#     #     print(b,'-->',a)
#     #     print(b,'-->',c)
#     #     print(a,'-->',c)
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
# move(3,'A','B','C')

# # 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
# 1.如果s为空，返回
# 2.从头开始判断每个字符是否为空，如果该字符为空，截取下一个字符进行判断直到不为空
# 2.从尾开始判断每个字符是否为空，如果该字符为空，截取上一个字符进行判断直到不为空
# def trim(s):
#     if len(s)==0:
#         return s
#     while s[0]==' ':
#         s=s[1:]
#         if len(s) == 0:
#             return s
#     while s[-1]==' ':
#         s=s[:-1]
#         if len(s)==0:
#             return s
#     return s

# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')


#     # 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
# def findMinAndMax(L):
#     if len(L) ==0:
#         return (None,None)
#     min=L[0]
#     max=L[0]
#     for n in L:
#         if min>n:
#             min=n
#         if max<n:
#             max=n
#     return (min,max)        


#     # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

# # 列出当前目录下的所有文件和目录名
# import os 
# print([d for d in os.listdir('.')])

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

# >>> L = ['Hello', 'World', 18, 'Apple', None]
# >>> [s.lower() for s in L]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# AttributeError: 'int' object has no attribute 'lower'
# 使用内建的isinstance函数可以判断一个变量是不是字符串：

# >>> x = 'abc'
# >>> y = 123
# >>> isinstance(x, str)
# True
# >>> isinstance(y, str)
# False
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

# l1=['RERER','YRYRT',21,'32323',None]
# # l2=[n.lower() for n in l1]
# l2=[]
# for n in l1:
#     if isinstance(n,str):
#         l2.append(n.lower())
#     else:
#         l2.append(n)
# print(l2)

# 斐波拉契数列

# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return 'done'

# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return 'done'

# g=fib(12)
# while True:
#     try:
#         x=next(g)
#         print('b',x)
#     except StopIteration as e:
#         print('generator return value',e.value)
#         break

# 杨辉三角定义如下：

#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：


# def triangles():
#     l=[1]
#     while True:
#         yield l
#         l=[1]+[l[n]+l[n+1] for n in range(len(l)-1)]+[1]

# # 期待输出:
# # [1]
# # [1, 1]
# # [1, 2, 1]
# # [1, 3, 3, 1]
# # [1, 4, 6, 4, 1]
# # [1, 5, 10, 10, 5, 1]
# # [1, 6, 15, 20, 15, 6, 1]
# # [1, 7, 21, 35, 35, 21, 7, 1]
# # [1, 8, 28, 56, 70, 56, 28, 8, 1]
# # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break

# for t in results:
#     print(t)

# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# 把str转化成int的函数
# from functools import reduce
# def fn(x,y):
#     return x*10+y

# def char2num(s):
#     digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return digits[s]

# val=reduce(fn,map(char2num,'98746621'))
# print(val)


# from functools import reduce
# DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def str2int(s):
#     def fn(x,y):
#         return x*10+y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn,map(char2num,s))

# val=str2int('98746621')
# print(val)

# from functools import reduce
# DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def char2num(s):
#     return DIGITS[s]
# def str2int(s):
#     return reduce(lambda  x,y:x*10+y,map(char2num,s))

# val=str2int('98746621')
# print(val)

# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def normalize(name):
#     name=name.lower()
#     name=name[0].upper()+name[1:]
#     return name    

# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# def normalize(name):
#     name=name.capitalize()
#     return name    

# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# from functools import reduce
# def prod(L):
#     def mul(x,y):
#         return x*y
#     return reduce(mul,L)
    
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# from functools import reduce
# def str2float(s):
#     def char2num(s):
#         DIGTS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#         return DIGTS[s]
#     def posfn(x,y):
#         return x*10+y
#     def negfn(v):
#         pass
#     pos=s.split('.')[0]
#     neg=s.split('.')[1]
#     return reduce(posfn,map(char2num,pos))+negfn(map(char2num,neg))

# from functools import reduce
# CHAR_TO_FLOAT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '.': -1
# }
# # point是转为负数的标志
# def str2float(s):
#     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
#     point = 0
#     def to_float(x, y):
#         nonlocal point
#         if y == -1:
#             point = 1
#             return x
#         if point == 0:
#             return x * 10 + y
#         else:
#             point = point * 10
#             return x + y / point
#     return reduce(to_float, nums, 0.0)



# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')


# 用filter求素数
# 埃拉托色尼筛选法
# 埃氏筛法步骤编辑
# （1）先把1删除（现今数学界1既不是质数也不是合数）

# （2）读取队列中当前最小的数2，然后把2的倍数删去
# （3）读取队列中当前最小的数3，然后把3的倍数删去
# （4）读取队列中当前最小的数5，然后把5的倍数删去
# （5）读取队列中当前最小的数7，然后把7的倍数删去
# （6）如上所述直到需求的范围内所有的数均删除或读取
# def _odd_iter():#生成器生成从3开始的无限奇数序列
#     n=1
#     while True:
#         n=n+2
#         yield n

# def _not_divisible(n):#定义筛选函数
#     return lambda x:x%n>0

# def primes():
#     yield 2
#     it=_odd_iter()#初始序列
#     while True:
#         n=next(it)#返回序列的第一个数
#         yield n
#         it=filter(_not_divisible(n),it)#构造新序列

# def main():
#     for n in primes():#构造循环条件
#         if n <1000:
#             print(n)
#         else:
#             break

# if __name__ == '__main__':
#     main()
# # 首先输出2
# # 经过primes函数，会去执行_not_divisible筛选出序列中的素数


# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
# # 字符串倒转
# def is_palindrome(n):
#     return str(n)==str(n)[::-1]

# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')



# 练习
# 假设我们用一组tuple表示学生名字和成绩：

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0]

# L2 = sorted(L, key=by_name)
# print(L2)

# 再按成绩从高到低排序：

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_score(t):
#     return t[1]

# L2 = sorted(L, key=by_score,reverse=True)
# print(L2)

# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

# def createCounter():
#     i=0
#     def counter():
#         nonlocal i
#         i+=1
#         return i
#     return counter

# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# 2. 如果使用闭包知识，且使用变量n（int对象），需要了解的是变量的作用域遵循LEGB规则，然后在counter()函数内声明nonlocal n

# 3. 如果使用闭包知识，且使用变量n（list对象），除了要理解LEGB规则外，还要明白python在函数内可以直接读取其他作用域范围的变量，但是修改变量时就会默认视为局部变量；在这种情况下n是变量名，我们使用的是n对应list对象（可变对象）的内容，变量n未被修改过，因此使用时不需要对n做nonlocal声明即可完成练习。


# 练习
# 请用匿名函数改造下面的代码：
# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))

# L = list(filter(lambda n:n%2==1, range(1, 20)))

# print(L)

# 打印日志的装饰器
# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():'% func.__name__)
#         return func(*args,**kw)
#     return wrapper

# @log
# def now():
#     print('qiufeihong')

# now()

# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kw):
#             print('%s %s():'%(text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator

# @log('hello')
# def now():
#     print('qiufeihong')

# now()#== now=log('hello')(now)
# print(now.__name__)


# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print('call %s():'%func.__name__)
#         return func(*args,**kw)
#     return wrapper



#  练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

# -*- coding: utf-8 -*-
# import time, functools
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         start = time.time()
#         fn(*args, **kw)
#         end = time.time()
#         print('%s executed in %.4f ms' % (fn.__name__, end - start))
#         return fn(*args, **kw)

#     return wrapper

# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')   



# # 面向对象编程
# class Student(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def print_age(self):
#         print('%s:%s'%(self.name,self.age))

# s1=Student('qiufeihong',12)
# s2=Student('qiu',42)
# s1.print_age()
# s2.print_age()

# s1={'name':'qiufeihong','age':12}
# s2={'name':'qiu','age':42}
# def print_age(st):
#     print('%s:%s'%(st['name'],st['age']))

# print_age(s1)
# print_age(s2)


# # 面向对象编程-访问限制
# class Student(object):
#     def __init__(self,name,age):
#         self.__name=name
#         self.age=age
#     def print_age(self):
#         print('%s:%s'%(self.name,self.age))

# s1=Student('qiu',12)
# print(s1.__name)
# # AttributeError: 'Student' object has no attribute '__name'


# 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender

#     def get_gender(self):
#         return self.__gender

#     def set_gender(self,gender):
#         if gender!='half-visible femal':
#             self.__gender=gender

# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
#     bart.set_gender('half-visible femal')
#     if bart.get_gender()=='half-visible femal':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# 判断对象
# import types
# def a():
#     pass
# print(type(a)==types.FunctionType)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(lambda x:x)==types.LambdaType)
# print(type(x for x in range(10))==types.GeneratorType)



# 练习
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

# class Student(object):
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         # 不能是self
#         Student.count=Student.count+1


# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')


# 使用@property隐藏属性
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#     @property
#     def gender(self):
#         return self.__gender
#     @gender.setter
#     def gender(self,gender):
#         if gender!='half-visible femal':
#             self.__gender=gender

# # 测试:
# bart = Student('Bart', 'male')
# if bart.gender != 'male':
#     print('测试失败!')
# else:
#     bart.gender='female'
#     if bart.gender != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
#     bart.gender='half-visible femal'
#     if bart.gender=='half-visible femal':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

# class Screen(object):
#     @property
#     def width(self):
#         return self.__width

#     @width.setter
#     def width(self,width):
#         self.__width=width

#     @property
#     def height(self):
#         return self.__height

#     @height.setter
#     def height(self,height):
#         self.__height=height

#     @property
#     def resolution(self):
#         return self.__width*self.__height


# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')


# 定制类
# __str__

# class Student(object):
#     def __init__(self,name):
#         self.name=name

# print(Student('qiufeihong'))
# <__main__.Student object at 0x000001E32CEE4248>


# class Student(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return 'Student object (name:%s)'%self.name

# print(Student('qiufeihong'))
# Student object (name:qiufeihong)

# __iter__

# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>1000:
#             raise StopIteration()
#         return self.a
    


# for n in Fib():
#     print(n)


# print(Fib()[5])
# TypeError: 'Fib' object is not subscriptable

# __getitem__
# class Fib(object):
#     def __getitem__(self,n):
#         a,b=1,1
#         for x in range(n):
#             a,b=b,a+b
#         return a
# f=Fib()
# print(f[0])
# # 1
# print(f[1000])
# # 70330367711422815821835254877183549770181269836358732742604905087154537118196933579742249494562611733487750449241765991088186363265450223647106012053374121273867339111198139373125598767690091902245245323403501
# print(f[0:10])
# # TypeError: 'slice' object cannot be interpreted as an integer


# 切片方法

# class Fib(object):
#     def __getitem__(self,n):
#         # 如果n是索引
#         if isinstance(n,int):
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         # 如果n是切片
#         if isinstance(n,slice):
#             start=n.start
#             stop=n.stop
#             if start is None:
#                 start=0
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x>=start:
#                     L.append(a)
#                 a,b=b,a+b
#             return L

# f=Fib()
# print(f[0])
# # 1
# print(f[1000])
# # 70330367711422815821835254877183549770181269836358732742604905087154537118196933579742249494562611733487750449241765991088186363265450223647106012053374121273867339111198139373125598767690091902245245323403501
# print(f[0:10])
# # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：

# from enum import Enum, unique
# # class Gender(Enum):
# #     Male = 0
# #     Female = 1
# Gender=Enum('Gender',('Male','Female'))

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

# # 测试:
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')


# type()
# def fn(self,name='world'):
#     print('hello,%s'%name)

# Hello=type('hello',(object,),dict(hello=fn))
# h=Hello()
# h.hello()

# print(type(Hello))
# print(type(h))


# 错误处理
# try:
#     print('try')
#     r=10/0
#     print('resulr',r)
# except ValueError as e:
#     print('valueError',e)
# finally:
#     print('finally')
# print('end')

# try
# finally
# Traceback (most recent call last):
#   File ".\function.py", line 856, in <module>
#     r=10/0
# ZeroDivisionError: division by zero


# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally...')


# main()
# # Error: division by zero
# # finally...


# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     bar('0')

# main()

# # Traceback (most recent call last):
# #   File ".\function.py", line 903, in <module>
# #     main()
# #   File ".\function.py", line 901, in main
# #     bar('0')
# #   File ".\function.py", line 898, in bar
# #     return foo(s) * 2
# #   File ".\function.py", line 895, in foo
# #     return 10 / int(s)
# # ZeroDivisionError: division by zero

# import logging
# def foo(s):
#     return 10/int(s)

# def bar(s):
#     return  foo(s)*2

# def main():
#     try:
#         bar(0)
#     except Exception as e:
#         logging.exception(e)

# main()
# # ERROR:root:division by zero
# # Traceback (most recent call last):
# #   File ".\function.py", line 925, in main
# #     bar(0)
# #   File ".\function.py", line 921, in bar
# #     return  foo(s)*2
# #   File ".\function.py", line 918, in foo
# #     return 10/int(s)
# # ZeroDivisionError: division by zero

# 练习
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：

# from functools import reduce

# def str2num(s):
#     return int(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# main()
# # 100 + 200 + 345 = 645
# # Traceback (most recent call last):
# #   File ".\function.py", line 959, in <module>
# #     main()
# #   File ".\function.py", line 956, in main
# #     r = calc('99 + 88 + 7.6')
# #   File ".\function.py", line 951, in calc
# #     return reduce(lambda acc, x: acc + x, ns)
# #   File ".\function.py", line 946, in str2num
# #     return int(s)
# # ValueError: invalid literal for int() with base 10: ' 7.6'


# 这说明`return int(s)`错了。
# 改成`return float(s)`即可。


# 单元测试
# class Dict(dict):
#     def __init__(self,**kw):
#         super().__init__(**kw)

#     def __getattr__(self,key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict'object has no  attribute '%s'="% key)


#     def __setattr__(self,key,value):
#         self[key]=value

# import unittest

# class TestDict(unittest.TestCase):
#     def setUp(self):
#         print('setUp...例如：登录')

#     def tearDown(self):
#         print('tearDown...例如：注销')
#     def test_init(self):
#         d=Dict(a=1,b='test')
#         self.assertEqual(d.a,1)
#         self.assertEqual(d.b,'test')
#         self.assertTrue(isinstance(d,dict))

#     def test_key(self):
#         d=Dict()
#         d['key']='value'
#         self.assertEqual(d.key,'value')

#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')

#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']

#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty

# if __name__=='__main__':
#     unittest.main()

# # .....
# # ----------------------------------------------------------------------
# # Ran 5 tests in 0.001s

# # OK


# 练习
# 对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：
# 错误
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score >= 60:
#             return 'B'
#         if self.score >= 80:
#             return 'A'
#         return 'C'

# 正确如下：

# import unittest
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score>100 or self.score<0:
#             raise ValueError
#         if self.score >= 80:
#             return 'A'
#         if self.score >= 60:
#             return 'B'
#         return 'C'

# class TestStudent(unittest.TestCase):

#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')

#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')

#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')

#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()

# if __name__ == '__main__':
#     unittest.main()

# # doctest来测试编写的Dict类：
# class Dict(dict):
#     '''
#     Simple dict but also support access as x.y style.

#     >>> d1 = Dict()
#     >>> d1['x'] = 100
#     >>> d1.x
#     100
#     >>> d1.y = 200
#     >>> d1['y']
#     200
#     >>> d2 = Dict(a=1, b=2, c='3')
#     >>> d2.c
#     '3'
#     >>> d2['empty']
#     Traceback (most recent call last):
#         ...
#     KeyError: 'empty'
#     >>> d2.empty
#     Traceback (most recent call last):
#         ...
#     AttributeError: 'Dict' object has no attribute 'empty'
#     '''
#     def __init__(self, **kw):
#         super(Dict, self).__init__(**kw)

#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

#     def __setattr__(self, key, value):
#         self[key] = value

# if __name__=='__main__':
#     import doctest
#     doctest.testmod()

# # 练习
# # 对函数fact(n)编写doctest并执行：

# def fact(n):
#     '''
#     Calculate 1*2*...*n
    
#     >>> fact(1)
#     1
#     >>> fact(10)
#     3628800
#     >>> fact(-1)
#     Traceback (most recent call last):
#     ...
#     ValueError
#     '''
#     if n < 1:
#         raise ValueError()
#     if n == 1:
#         return 1
#     return n * fact(n - 1)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()


# # 练习
# # 请将本地一个文本文件a写入“hello”，并打印出来：

# fpath = r'D:\a.txt'

# with open(fpath,'w') as f:
#     f.write('hello')

# with open(fpath, 'r') as f:
#     s = f.read()
#     print(s)



# 练习
# # 利用os模块编写一个能实现dir -l输出的程序。
# # dir -l：输出所有当前目录下的文件和子文件
# import os

# def List_FileAndDir(fd):
#      print(os.path.relpath(fd))     #打印相对路径
#      if os.path.isfile(fd):
#           return
#      for fname in os.listdir(fd):    #遍历子目录
#           List_FileAndDir(os.path.join(fd,fname))
# List_FileAndDir('.')     # '.' 从当前目录开始

# # 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

# import os

# path= input('输入查询路径:')
# xun=input('请输入要查询的文件包含的字符串:')
# def finpath(path):
#     for x in os.listdir(path):
#         mypath=os.path.abspath(os.path.join(path,x))
#         if os.path.isfile(mypath):
#             if mypath.find(xun) != -1:
#                 print('找到文件',x)
#                 print('路径',mypath)
#         else:
#             finpath(mypath)

# finpath(path)


# # 练习
# # 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：

# # -*- coding: utf-8 -*-

# import json
# obj = dict(name='小明', age=20)
# s = json.dumps(obj, ensure_ascii=True)
# # s = json.dumps(obj, ensure_ascii=False)

# print(s)
# # {"name": "\u5c0f\u660e", "age": 20}
# # {"name": "小明", "age": 20}
# # ensure_ascii默认情况是True，这时会把中文转成Unicode码，设置成False的话就是打印中文


# # window多进程

# from multiprocessing import Process
# import os

# def run_proc(name):
#     print('run child process %s (%s)……' % (name,os.getpid()))

# if __name__=='__main__':
#     print('parent process %s'% os.getpid())
#     p=Process(target=run_proc,args=('test',))
#     print('child process will start')
#     p.start()
#     p.join()
#     print('child process end')

# # parent process 20580
# # child process will start
# # run child process test (4220)……
# # child process end

# # 用进程池的方式批量创建子进程

# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(10)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')


# # Parent process 19312.
# # Waiting for all subprocesses done...
# # Run task 0 (11244)...
# # Run task 1 (16428)...
# # Run task 2 (9804)...
# # Run task 3 (2112)...
# # Run task 4 (3276)...
# # Task 3 runs 0.40 seconds.
# # Task 4 runs 0.70 seconds.
# # Task 0 runs 1.11 seconds.
# # Task 1 runs 1.85 seconds.
# # Task 2 runs 2.98 seconds.
# # All subprocesses done.



# # 以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

# from multiprocessing import Process, Queue
# import os, time, random

# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)

# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

# from multiprocessing import Process, Queue
# import os, time, random

# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)

# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

# # Process to write: 21408
# # Put A to queue...
# # Process to read: 6936
# # Get A from queue.
# # Put B to queue...
# # Get B from queue.
# # Put C to queue...
# # Get C from queue.


# 多线程
# import time, threading

# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
# # thread MainThread is running...
# # thread LoopThread is running...
# # thread LoopThread >>> 1
# # thread LoopThread >>> 2
# # thread LoopThread >>> 3
# # thread LoopThread >>> 4
# # thread LoopThread >>> 5
# # thread LoopThread ended.
# # thread MainThread ended.



# import time, threading

# # 假定这是你的银行存款:
# balance = 0

# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#         change_it(n)

# t1 = threading.Thread(target=run_thread, args=(5,))
# print('balance-t1',balance)

# t2 = threading.Thread(target=run_thread, args=(8,))
# print('balance-t2',balance)

# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('balance',balance)

# # balance-t1 0
# # balance-t2 0
# # balance 5


# # 多线程加锁
# import time, threading

# balance = 0
# lock = threading.Lock()

# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()
            
# t1 = threading.Thread(target=run_thread, args=(5,))
# print('balance-t1',balance)

# t2 = threading.Thread(target=run_thread, args=(8,))
# print('balance-t2',balance)

# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('balance',balance)
# # balance-t1 0
# # balance-t2 0
# # balance 0


# # 死循环
# import threading, multiprocessing

# def loop():
#     x = 0
#     while True:
#         x = x ^ 1

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()



# 练习
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

# import re
# def is_valid_email(addr):
#     re_email= re.compile('^[\w\.]+?@[\w]+\.com$')
#     msg =re_email.match(addr)
#     if msg==None:
#         return False
#     else:
#         return True

# # 测试:
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')


# # 可以提取出带名字的Email地址：

# # <Tom Paris> tom@voyager.org => Tom Paris
# # bob@example.com => bob

# import re
# def name_of_email(addr):
#     # re_email=re.compile('^(.*?)[\w\s]+?@[\w]+\.org$')
#     re_email=re.compile('^(.*?)([a-zA-Z\s]+)(.*)$')
#     res=re_email.match(addr).groups()
#     return res[1]

# # 测试:
# assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
# print('ok')

# # 匹配任意字符-匹配字母和空格-匹配任意字符

# # 练习
# # 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

# import re
# from datetime import datetime, timezone, timedelta
# def to_timestamp(dt_str, tz_str):
#     # 转化为当前时间的datetime
#     dt= datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
#     # 时分截取
#     timeSp=re.split(r'[\+\-\:]',tz_str)
#     # 小时
#     hourSp=timeSp[1]
#     # 分钟
#     minuteSp=timeSp[2]
#     # 正负值
#     ope=tz_str[3]
#     # 小时偏移量
#     hourOffset=int(ope+hourSp)
#     # 分钟偏移量
#     minuteOffset=int(ope+minuteSp)
#     # 利用得到的偏移时差创建输入的dt_str的实际时区
#     tz_utc=timezone(timedelta(hours=hourOffset,minutes=minuteOffset))
#     # 调用replace强行将其换为刚才得到的时区，最后调用timestamp，自动转换为UTC时间戳
#     return dt.replace(tzinfo=tz_utc).timestamp()
# # 测试:
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# print(t1)
# assert t1 == 1433121030.0, t1

# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# print(t2)
# assert t2 == 1433121030.0, t2

# print('ok')

# # 练习
# # 请写一个能处理去掉=的base64解码函数：

# import base64
# def safe_base64_decode(s):
#     if type(s)==bytes:
#         s=str(s,encoding='utf-8')
#     if len(s)%4==0:
#         return base64.b64decode(s)
#     else:
#         return base64.b64decode(s+'='*(4-(len(s)%4)))

# # 测试:
# assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
# assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
# print('ok')


# # 练习
# # 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。

# import base64, struct
# bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
#                    'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
#                    '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
#                    'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
#                    '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
#                    '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
#                    'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
#                    '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
#                    '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
#                    'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
#                    'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
#                    '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
# def bmp_info(data):
#     info=struct.unpack('<ccIIIIIIHH', data[:30])
#     return {
#         'width': info[-4],
#         'height':info[-3],
#         'color': info[-1]
#     }

# # 测试
# bi = bmp_info(bmp_data)
# assert bi['width'] == 28
# assert bi['height'] == 10
# assert bi['color'] == 16
# print('ok')

# # 读入前30个字节来分析




# # 练习
# # 根据用户输入的口令，计算出存储在数据库中的MD5口令：
# # 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
# # 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
# import hashlib
# def calc_md5(password):
#     md5=hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     return md5.hexdigest()

# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
# def login(user, password):
#     p=calc_md5(password)
#     if db[user]==p:
#         return True
#     else:
#         return False

# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')



# # 练习
# db = {}

# def register(username, password):
#     db[username] = get_md5(password + username + 'the-Salt')
# # 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

# # 然后，根据修改后的MD5算法实现用户登录的验证：

# import hashlib, random

# def get_md5(s):
#     return hashlib.md5(s.encode('utf-8')).hexdigest()

# class User(object):
#     def __init__(self, username, password):
#         self.username = username
#         self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
#         self.password = get_md5(password + self.salt)
# db = {
#     'michael': User('michael', '123456'),
#     'bob': User('bob', 'abc999'),
#     'alice': User('alice', 'alice2008')
# }
# def login(username, password):
#     user = db[username]
#     return user.password == get_md5(password+ user.salt)

# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')

# # 这个函数里的password是用户新传入的password，不是创建User实例是带入的，所以起到了对比作用，可以看出输入的是不是该用户的密码；


# # 练习
# # 将上一节的salt改为标准的hmac算法，验证用户口令：

# import hmac, random

# def hmac_md5(key, s):
#     return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

# class User(object):
#     def __init__(self, username, password):
#         self.username = username
#         self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
#         self.password = hmac_md5(self.key, password)

# db = {
#     'michael': User('michael', '123456'),
#     'bob': User('bob', 'abc999'),
#     'alice': User('alice', 'alice2008')
# }
# def login(username, password):
#     user = db[username]
#     return user.password == hmac_md5(user.key, password)

# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')


# # 练习
# # 计算圆周率可以根据公式：

# # 利用Python提供的itertools模块，我们来计算这个序列的前N项和：

# import itertools
# def pi(N):
#     ' 计算pi的值 '
#     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
#     natuals = itertools.count(start=1,step=2)
#     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
#     ns = itertools.takewhile(lambda x:x<=2*N-1, natuals)
#     lns=list(ns)
#     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
#     sum=0
#     for item in lns:
#         tmp=4/(item*(-1)**(item//2))
#         sum+=tmp
#     # step 4: 求和:
#     return sum

# # 测试:
# print(pi(10))
# print(pi(100))
# print(pi(1000))
# print(pi(10000))
# assert 3.04 < pi(10) < 3.05
# assert 3.13 < pi(100) < 3.14
# assert 3.140 < pi(1000) < 3.141
# assert 3.1414 < pi(10000) < 3.1415
# print('ok')



# # 练习：
# # 请利用SAX编写程序解析XML格式的天气预报，获取天气预报：
# # 功能：获取浙江省所有地区的当天天气预报信息
# from xml.parsers.expat import ParserCreate            # 引入xml解析模块
# from urllib import request                            # 引入URL请求模块

# class WeatherSaxHandler(object):                      # 定义一个天气事件处理器

#     weather ={'city':1,'cityname':[], 'forecast':[]}               # 初始化城市city和预报信息forecast

#     def start_element(self, name, attrs):             # 定义开始标签处理事件
#         if name=='zhejiang':
#             self.weather['city']='浙江'
#         if name == 'city':               # 获取location信息
#             self.weather['cityname'].append(attrs['cityname'])          #获取地区名
#             # 获取forecast信息
#             self.weather['forecast'].append({
#                 'state':attrs['stateDetailed'], 
#                 'high':attrs['tem2'], 
#                 'low':attrs['tem1'],
#                 'windDir':attrs['windDir'],
#                 'windPower':attrs['windPower'],
#                 'windState':attrs['windState']
#             })

# def parseXml(xml_str):                                # 定义xml解析器

#     handler = WeatherSaxHandler()
#     parser = ParserCreate()
#     parser.StartElementHandler = handler.start_element
#     parser.Parse(xml_str)                             # 解析xml文本
#     print('City'+handler.weather['city'])
#     for (x,y) in zip(handler.weather['cityname'],handler.weather['forecast']):             # 打印天气信息
#         print('Region:'+x)
#         print(y)
       
#     return handler.weather
    

# # 测试:
# URL = 'http://flash.weather.com.cn/wmaps/xml/zhejiang.xml'

# with request.urlopen(URL, timeout=4) as f:
#     data = f.read()

# result = parseXml(data.decode('utf-8'))


# # 练习
# # 缩放图片,模糊图片
# from PIL import Image,ImageFilter
# im=Image.open('wordcloud2.png')
# w,h=im.size
# print('origin image size:%sx%s'%(w,h))
# im.thumbnail((w//2,h//2))
# print('resize image to:%sx%s'%(w//2,h//2))
# im.save('wordcloud3.png','png')
# im2=Image.open('coronavirus_test_2.png')
# im2.filter(ImageFilter.BLUR)
# im2.save('wordcloud4.png','png')

# # 练习
# # 生成字母验证码图片
# from PIL import Image, ImageDraw, ImageFont, ImageFilter

# import random
# # 随机字母:传入一个数值,返回这个数值对应的ascii码字符
# def rndChar():
#     return chr(random.randint(65,90))
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# # 240 x 60:
# width = 60 * 6
# height = 60
# # 创建新的图片
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('msyh.ttc', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(6):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('code.png', 'png')


# # 练习
# from tkinter import *
# import tkinter.messagebox as messagebox
# class Application(Frame):
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#     def createWidgets(self):
#         self.nameInput=Entry(self)
#         self.nameInput.pack()
#         self.alertButton=Button(self,text='hello',command=self.hello)
#         self.alertButton.pack()
#     def hello(self):
#         name=self.nameInput.get() or 'world'
#         messagebox.showinfo('message','hello,%s'% name)
# app=Application()
# # 窗口标题
# app.master.title('hello world')
# # 主消息循环:
# app.mainloop()

# # https://docs.python.org/2/library/tkinter.html


# #练习
# #画一个正方形
# from turtle import *
# width(6)
# forward(200)
# right(90)
# pencolor('red')
# forward(200)
# right(90)
# pencolor('green')
# forward(200)
# right(90)
# pencolor('yellow')
# forward(200)
# right(90)
# done()

# # https://docs.python.org/3.3/library/turtle.html#turtle-methods


# #练习
# #画一个五角星
# from turtle import *
# def drawStar(x,y):
#     pu()
#     goto(x,y)
#     pd()
#     seth(0)
#     for i in range(5):
#         fd(40)
#         rt(144)
# for x in range(0,250,50):
#     drawStar(x,0)
# done()


# #练习
# #复杂树
# from turtle import *

# # 设置色彩模式是RGB:
# colormode(255)

# lt(90)

# lv = 14
# l = 120
# s = 45

# width(lv)

# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)

# penup()
# bk(l)
# pendown()
# fd(l)

# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()

#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)

#     l = 3.0 / 4.0 * l

#     lt(s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)

#     # restore the previous pen width
#     width(w)

# speed("fastest")

# draw_tree(l, 4)

# done()

# #练习
# #新浪socket-新浪的首页

# import socket

# # 创建一个socket:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # 建立连接:
# s.connect(('www.sina.com.cn', 80))

# # 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break

# data = b''.join(buffer)

# # 关闭连接:
# s.close()

# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))

# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

