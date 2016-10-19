# if-else.py
# 条件判断

# elif 等于 else if

if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>

# if语句是从上往下判断，如果某个判断为True，则把判断对应的执行语句执行后，就忽略掉剩下的elif和else

age = 21
if age >= 6:
   print('teenager')
elif age >= 18:
   print('adult')
else:
   print('kid')
