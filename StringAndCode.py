# StringAndCode.py
# 字符串和编码

# 字符串

print('Python 派森')
# Python 派森

# 对于单个字符编码
# ord()函数获取字符的整数显示
ord('A')
# 65
ord('中')
# 20013

# chr()函数把编码转换为对应的字符
chr(65)
# 'A'
chr(20013)
# '中'

# 16进制
'\u4e2d\u6587'
# '中文'

# Python对 bytes 类型的数据用带 b 前缀的单引号或双引号表示
x = b'ABC'
# 'ABC' 和 b'ABC' 虽然显示的内容一样，但是 bytes 类型每个字符只占一个字节

# str -> 指定的bytes 用 encode()方法
'ABC'.encode('ascii')
# b'ABC'
'中文'.encode('utf-8')
# b'\xe4\xb8\xad\xe6\x96\x87'

# bytes -> str 用 decode()方法
b'ABC'.decode('ascii')
# 'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
# '中'

# len() 函数计算str有多少个字符
len('ABC')
# 3
len('中文')
# 2

# 若换成 bytes ，len() 则计算字节数
len(b'ABC')
# 3
len(b'\xe4\xb8\xad\xe6\x96\x87')
# 6



# 格式化

# 方式和C语言一致
'Strive for %s, %d.' %('Greatness', 13)
# Strive for Greatness, 13.

# 格式化整数和浮点数可以指定是否补0和整数和小数的位数
'%2d-%02d' % (3, 1)
# ' 3-01'
'%.5f' % 3.141592654
# '3.14159'

# %s 可以把任何数据类型转换为字符串
# %% 表示 %


