'''
1、可变的默认参数
'''


def func01(element, to=[]):
    to.append(element)
    return to


print(func01('a'))
print(func01('b'))
'''
第一次输出是['a']   没问题
第二次输出是['a','b']   和预期结果不一样了
为什么呢？
在python中，默认参数仅会在第一次调用时生成，后续调用都不会生成了。
如果需要每次都生成，则需要换一种写法
'''


def func02(element, to=None):
    if to == None:
        to = []
    to.append(element)
    return to


'''
2、闭包
'''


def func03():
    inner_list = []
    for i in range(5):
        def func04(x):
            return i * x
        inner_list.append(func04)
    return inner_list


for f in func03():
    print(f(2))

'''
输出的是5个8，这就是闭包导致的。
变量查找顺序：local、enclousing、global、builtin
闭包中，local找不到了，就去找enclousing，而enclousing是迟绑定的，当获取这个值的时候，for循环已经完成了，内部函数只能拿到最后一次的值：4
'''


def func03_01():
    return [lambda x : i * x for i in range(5)]

def func03_02():
    return (lambda x : i * x for i in range(5))

def func03_03():
    inner_list = []
    for i in range(5):
        def func04(x,i=i):
            return i * x
        inner_list.append(func04)
    return inner_list
'''
上面三个函数中：
01是原函数的压缩写法，返回值仍为5个8
02是用括号将构造式括起来，变成了生成器（不是转成元组哦）。生成器是惰性求值（找他要才给值），所以每次内部函数都能获得一个新值
03是用i这个变量接收了外部的变量i，转换成了局部变量（局部变量的优先级要高于闭包，这里的i=i换成k=i就更好理解）
def func03_04():
    inner_list = []
    for i in range(5):
        def func04(x,k = i):
            return k * x
        inner_list.append(func04)
    return inner_list
'''
'''
闭包的定义：
在计算机科学中，闭包（英语：Closure），又称词法闭包（Lexical Closure）或函数闭包（function closures），是引用了自由变量的函数。
这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。
所以，有另一种说法认为闭包是由函数和与其相关的引用环境组合而成的实体。
闭包在运行时可以有多个实例，不同的引用环境和相同的函数组合可以产生不同的实例。
一个函数和其外部的非全局变量共同构成了闭包
比如
def a():
    l = []
    def b(x):
        l.append(x)
        print(l)
    return b

c = a()
d = a()
c(1)   # output： [1]
c(2)   # output： [1, 2]
d(1)   # output： [1]
d(2)   # output： [1, 2]
c(3)   # output： [1, 2, 3]
d(3)   # output： [1, 2, 3]
c(4)   # output： [1, 2, 3, 4]
c(5)   # output： [1, 2, 3, 4, 5]

这就构成了一个闭包
完成闭包，需要函数使用了外部的变量（即在def b(x)中使用了外部变量l）
'''