# Loop.py
# 循环

# for in 循环

# for x in ... 循环就是把每个元素代入变量x，然后执行缩进块的语句
# 可以通过此方法 遍历 list 或 tuple 中的元素

balls = ['basketball', 'football', 'baseball']
for ball in balls:
    print(ball)
# 执行这段代码会依次打印balls的每一个元素
# basketball
# football
# baseball

# range() 函数，可以生成一个整数序列
list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
for x in range(101):
    sum = sum + x
print(sum)
# 5050


# while 循环
# 条件满足则不断循环，条件不满足则退出循环

sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)
# 5050
