# -*- coding: UTF-8 -*-

# Filename : 04-password.py
# author by : （学员ID)

# 要点：初步理解列表，了解密码生成的方式
import random

# 练习一
# 集中数字型密码生成方式
# 四位数字密码 PIN
print('\n---cutting line 1---')
for i in range(1,3):
    # for body begin ----
    password = random.randint(0,9999)
    print ('Password is : %04d' % (password))
    # for body end ----

# 练习二
# 集中数字型密码生成方式
# 四位数字密码 PIN
print('\n---cutting line 2---')
nums = ['0','1','2','3','4','5','6','7','8','9']
password = []
for i in range(1,5):
    # for body begin ----
    password.append(random.choice(nums))
    # debug
    print ('debug - Password list changing : %s' % (password))
    # for body end ----
# debug
print ('debug - list of password = %s' % (password))

# 顺序取出所有数字组成最终密码
print ('Password is : ', end='')
for item in password:
    print ('%s' % (item), end='')

# 练习三
# 混合型密码生成方式
# 数字 + 大小写 + 符号
print('\n\n---cutting line 3---')
# 定义所有可用的字符
char1 = ['0','1','2','3','4','5','6','7','8','9']
char2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
char4 = ['~','!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']',':','"',';','<','>','?',',','.','/']
# 合并到一个打的列表中去
charAll = char1 + char2 + char3 + char4
#debug
print('debug - All usable chars: %s' % (charAll))

# 定义密码的长度
pwdLen = 8

# 初始化清空最终密码
password = []
for i in range(1,pwdLen):
    # for body begin ----
    password.append(random.choice(charAll))
    # debug
    print ('debug - Password list changing : %s' % (password))
    # for body end ----
# debug
print ('debug - list of password = %s' % (password))

# 顺序取出所有数字组成最终密码
print ('\nPassword is : ', end= '')
for item in password:
    print ('%s' % (item), end='')
