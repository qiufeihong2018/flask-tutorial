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
def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
    # elif n==2:
    #     print(a,'-->',b)
    #     print(a,'-->',c)
    #     print(b,'-->',c)
    # elif n==3:
    #     print(a,'-->',c)
    #     print(a,'-->',b)
    #     print(c,'-->',b)
    #     print(a,'-->',c)
    #     print(b,'-->',a)
    #     print(b,'-->',c)
    #     print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(3,'A','B','C')