# ListAndTuple.py 

# list

balls = ['basketball', 'Volleyball', 'football']
balls
# ['basketball', 'Volleyball', 'football']

# 用len() 函数可以获得list元素的个数
len(balls)
# 3

# 用索引来访问list中每一个位置的元素，索引从0开始
balls[0]
# 'basketball'
balls[1]
# 'Volleyball'
balls[2]
# 'football'

# 最后一个元素的索引是 len(balls) - 1， 若超出范围，会报 indexError。

# 获取最后一个元素可以用 -1 做索引，以此类推，可以获取倒数第n个
balls[-1]
# 'football'
balls[-2]
# 'Volleyball'

# 添加元素到 list
# 1 append() 添加到末尾
balls.append('baseball')
balls
# ['basketball', 'Volleyball', 'football', 'baseball']

# 2 insert() 插入到指定位置
balls.insert(1, 'handball')
balls
# ['basketball', ‘handball', 'Volleyball', 'football', 'baseball']


# 删除list的元素
# 1 pop() 删除末尾的元素
balls.pop()
balls
# ['basketball', ‘handball', 'Volleyball', 'football']

# 2 pop(i) 删除指定位置的元素 i为索引
balls.pop(1)
balls
# ['basketball', Volleyball', 'football']

# 替换list的元素，直接赋值给对应的索引位置
balls[1] = 'baseball'
balls
# ['basketball', 'baseball', 'football']

# list里面的元素数据类型可以不同
temp = ['Apple', 123, True]

# list可以看成二维数组
a = ['Apple', 'Facebook']
b = ['Twttier', p, 'Tencent', 'Google']
# 要拿到'Apple' 可以写 a[0] 或者 b[1][0]

# 空list
L = []
len(L)
# 0


