#__author: Liu Zheng
#date:2018/7/6

# def foo():
#     print('ok')
#
#     yield 1
#
#     print('ok2')
#
#     yield 2
#迭代器可以调用next方法
# for i in foo():   可迭代对象：内部有Iter函数   生成器  迭代器
#     while True:
#         i=next(foo)

def fib(max):
    n,before,after,=0,0,1
    while n < max:
        print(before)
        before,after = after,before+after  #先计算右边b+a 之后再赋值
        # #tmp = b
        # b=a
        # a=tmo+a
        n=n+1
fib(8)