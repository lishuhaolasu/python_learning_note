# Cython学习笔记

---

## 初次编译

---

### 指定Python版本

在使用Cython时，Cython会默认Python版本为2，需要在脚本头部写入以下声明
`# cython: language_level=3`

### 编写Python版本

随便写个helloworld好了,保存成helloworld.pyx
注意是pyx不是py

#### 小提示

* .pyx是Cython编写而成的Python扩展源代码，里面可能会写c风格的代码。
* .py也可以被编译成pyd(并不是所有拓展名都能进行编译哦)

```python
def func():
    print('HelloWorld!')
```

### 编写setup.py

```python
from distutils.core import setup
from Cython.Build import cythonize
setup(
    ext_modules = cythonize('test.py')
)
```

### 执行编译

运行下面代码就能执行编译操作了。inplace参数一定别忘了，不加不替换老的pyd

```batch
python .\setup.py build_ext --inplace
```
