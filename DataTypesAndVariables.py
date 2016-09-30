# DataTypesAndVariables.py

# 字符串

print('I\'m ok. ')
# I'm ok.
print('I\'m learning\nPython.')
# I'm learning
# Python
print('\\\n\\')
# \
# \

# 如果字符串内部有很多字符需要转义，需要加很多的'\'
print('\\\t\\')
# \     \

# 使用 r‘’ 表示 ‘’ 里面的字符串默认不转义
print(r'\\\t\\')
# \\\t\\

# 使用 '''...''' 的格式来表示多行内容
print('''line1 ... line2 ... line3''')
# line1
# line2
# line3


# 布尔值

# 可以直接用 True、False 表示布尔值，但是要注意大小写
True
# True
False
# False
3 > 2
# True
3 > 4
# False

# 布尔值可以用 and、or 和 not 运算

5 > 3 and 3 > 2
# True

5 > 3 or 2 > 3
# True

not True
# False

not False
# True

if age >= 18
    print('adult')
else
    print('teenager')


# 空值
# 用 None 表示，None 是一个特殊的空值


# 变量

a = 1
# 变量 a 是一个整数

b = 'Python'
# 变量 b 是一个字符串

Answer = True
# 变量 Answer 是一个布尔值

# 等号 = 是赋值语句，可以将任意数据类型赋值给变量，同一个变量可以反复赋值，可以是不同数据类型的变量

a = 123 # a 是整数
a = 'nba' # a 变为字符串


# 常量

# 通常用全部大写的变量名表示常量
PI = 3.141592654


# Python 中的除法

10 / 3
# 3.333333333335
9 / 3
# 3.0
# / 除法结果是浮点数，即使整除结果也是浮点数

10 // 3
# 3
# // 除法的结果永远是整数

10 % 3
# 1
# 求余数
