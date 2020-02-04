# https://www.liaoxuefeng.com/wiki/1016959663602400/1017316949097888
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


def triangles():
    l=[1]
    while True:
        yield l
        l=[1]+[l[n]+l[n+1] for n in range(len(l)-1)]+[1]

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')