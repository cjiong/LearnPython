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
