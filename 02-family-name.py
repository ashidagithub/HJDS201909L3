# -*- coding: UTF-8 -*-

# Filename : 02-family-name.py
# author by : （学员ID)

# 要点：初步理解列表和元组的常规操作

import random

# 练习一， 指定挑选一个姓并显示
print('\n---华丽分割线---练习（1）---')
family_words = ("赵","钱","孙","李","周","吴","郑","王")
print("%s" % (family_words[0]))

pos = 5 # 位置
print("我要第 (%d) 个姓，它是 %s" % (pos + 1, family_words[pos])) # 要注意以 0 开头

# 练习二： 遍历所有的姓
print('\n---华丽分割线---练习（2）---')
for name in family_words:
    print("%s " % name, end="")

# 练习三：随机挑选一个姓，产生n遍以上 - 随机生成 pos 方法
print('\n\n---华丽分割线---练习（3）---')
for i in range(3):
    pos = random.randint(0, 7)
    print("随机产生第 (%d) 个姓，它是 %s" % (i, family_words[pos])) # 要注意以 0 开头

# 练习四：随机挑选一个姓，产生n遍以上 - 随机生成 pos 方法 - 变量化
print('\n---华丽分割线---练习（4）---')
family_words = ( "赵","钱","孙","李","周","吴","郑","王" )

times = 5
print('总共有 %d 个姓供挑选，计划挑选 %d 次' % (len(family_words), times))
for i in range(times):
    #pos = random.randint(0, len(family_words)-1)
    #print("第 (%d) 次挑选姓，它是 %s" % (i, family_words[pos])) # 要注意以 0 开头
    print('picked familly name is : %s' % (random.choice(family_words)))
