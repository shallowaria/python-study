# 序列：list tuple? range? # array Set
# 映射： dict # object Map

result = [x for x in range(10) if x % 2 == 0] # 列表推导式，生成一个包含0-9中所有偶数的列表
print(result)

# 列表常用的方法 可变序列
list_demo = ['a', 'b', 'c', 'd', 'e', ['f', 'g']]
list_demo.insert(1, 'x') # 在列表的索引1位置插入一个元素'x'
list_demo.append('h') # 在列表末尾添加一个元素'h'
list_demo.extend(['i', 'j']) # 在列表末尾添加一个列表['i', 'j']中的所有元素
print(list_demo) # ['a', 'x', 'b', 'c', 'd', 'e', ['f', 'g'], 'h', 'i', 'j']
list_demo.remove('c') # 从列表中删除第一个出现的元素'c'
list_demo.pop(2) # 从列表中删除索引为2的元素，并返回该元素
list_demo.copy() # 返回列表的一个浅复制
list_demo.clear() # 删除列表中的所有元素

# 元组常用的方法
# 元组：创建后不可修改的对象,即不可变序列，所以所有修改序列元素的函数都无法使用
# () 或 tuple() 创建元组 del删除元组
tuple_demo = ('x', 'y', 'z')
tuple_demo.append('x') # AttributeError: 'tuple' object has no attribute 'append'
tuple_demo.remove('y') # AttributeError: 'tuple' object has no attribute 'remove'

# 集合：set frozenset 可变和不可变  不可重复，可用于去重
set_demo = {1, 2, 3, 4, 5}
set_demo.add(6) # 向集合中添加一个元素6
set_demo.update({7, 8}) # 向集合中添加一个集合{7, 8}中的所有元素
set_demo.remove(3) # 从集合中删除一个元素3，如果元素不存在会抛出KeyError
set_demo.discard(4) # 从集合中删除一个元素4，如果元素不存在不会抛出异常
# 字典 键和值，键必须是不可变类型，值可以是任意类型
dict_demo = {'a': 1, 'b': 2, 'c': 3}
dict_demo['d'] = 4 # 向字典中添加一个键值对 'd': 4
dict_demo.update({'e': 5, 'f': 6}) # 向字典中添加一个字典 {'e': 5, 'f': 6} 中的所有键值对
dict_demo.pop('b') # 从字典中删除一个键值对 'b': 2，并返回该值

dict_demo.items() # 返回一个包含字典中所有键值对的视图对象
dict_demo.keys() # 返回一个包含字典中所有键的视图对象
dict_demo.values() # 返回一个包含字典中所有值的视图对象

# [, default] = 👉 “这个参数可以不写，写了就用，不写就用默认值（None）”
dict_demo.setdefault('a', 0) # 如果键'a'不存在，则添加键值对 'a': 0，否则返回现有的值1