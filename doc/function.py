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

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
1.如果s为空，返回
2.从头开始判断每个字符是否为空，如果该字符为空，截取下一个字符进行判断直到不为空
2.从尾开始判断每个字符是否为空，如果该字符为空，截取上一个字符进行判断直到不为空
def trim(s):
    if len(s)==0:
        return s
    while s[0]==' ':
        s=s[1:]
        if len(s) == 0:
            return s
    while s[-1]==' ':
        s=s[:-1]
        if len(s)==0:
            return s
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')