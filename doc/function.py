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