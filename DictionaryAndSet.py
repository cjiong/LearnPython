# DictionaryAndSet.py

# dict

d = ['Harden': 13, 'Lebron': 23, 'Tracy': 1]
d['Harden']
# 13

# 将数据放入 dict，可以通过 key 的方式放入
d['Westbrook'] = 0
d['Westbrook']
# 0

# 一个 key 只能对应一个 value，多次对一个 key 放入 value，后面的值会把前面的值冲掉
d['Kobe'] = 8
d['Kobe']
# 8
d['Kobe'] = 24
d['Kobe']
# 24
d
# ['Harden': 13, 'Lebron': 23, 'Tracy': 1, 'Kobe':24]

# 若key不存在，dict会报错

# 判断key是否存在
# 1. 通过 in 判断key是否存在
'Durant' in d
# False

# 2. 通过dict提供的get方法，如果key不存在，返回None或者自己指定的值
d.get('Durant')
d.get('Durant', -1)
# -1

# 输出一个key，使用pop(key)方法
d.pop('Kobe')
d
# ['Harden': 13, 'Lebron': 23, 'Tracy': 1]


# set

# set和dict类似，是一组key的集合，但不存储value
# set中的key不能重复

# 创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
s
# [1, 2, 3]

# 重复元素在set中自动过滤
s = set([1, 1, 2, 2, 3, 3])
s
# [1, 2, 3]

# 通过add(key)方法添加元素到set中，可以重复添加，但是没有效果
s.add(4)
s
# [1, 2, 3, 4]
s.add(4)
s
# [1, 2, 3, 4]

# 通过remove(key)方法删除元素
s.remove(4)
s
# [1, 2, 3]

# 两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
# [2, 3]
s1 | s2
# [1, 2, 3, 4]





























