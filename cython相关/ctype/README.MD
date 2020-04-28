# Cython学习笔记

---

## C风格的代码

---

### 抄个示例

[积分函数](http://docs.cython.org/en/latest/src/quickstart/cythonize.html#typing-variables "官方教程" ),
这是官方教程提供的一个积分实现方式，提供了python和Cython两种实现。(加了个时间显示)

```python
import time
def f(x):
    return x**2 - x
def intergrate_f(a, b, N):
    start_time = time.time()
    s = 0
    dx = (b-a) / N
    for i in range(N):
        s += f(a+i*dx)
    ret = s*dx
    print(time.time()-start_time)
    return ret
```

```cython
import time
def f(double x):
    return x ** 2 - x
def intergrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx, ret, start_time
    start_time = time.time()
    s = 0
    dx = (b-a) / N
    for i in range(N):
        s += f(a+i*dx)
    ret = s*dx
    print(time.time()-start_time)
    return ret
```

### 编译

步骤就不写了，放俩文件里，编译两次先

### 运行

传参 10000,10000,1100000后
python实现耗时3000ms左右
Cython实现耗时900ms左右
速度有极大提升

### 代码分析

两部分代码几乎没有区别，最大的区别在于Cython的实现中，对所有变量进行了类型指定。这个过程极大的加快了速度。
以后写Cython要对变量类型进行指定！
