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