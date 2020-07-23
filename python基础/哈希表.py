'''
dict 和 set都是哈希集合。
dict是典型的哈希集合，键值对清晰
set是不典型的哈希集合，只有键没有值
哈希集合的特点是键不允许重复，所以set可以用来进行数据排重
下面，我们定义一个哈希集合
'''
class MyHashTable:
    
    def __init__(self,item):
        self.item = item
    
    def __hash__(self):
        return hash(self.item)
    
    def __eq__(self,other):
        if isinstance(other,self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

a = MyHashTable('a')
b = MyHashTable('b')
c = MyHashTable('c')

'''
哈希集合要有以下特征：
1：定义了__eq__和__hash__方法
2：__hash__ 方法要返回一个int值
3：__eq__ 进行判断是否相同
'''