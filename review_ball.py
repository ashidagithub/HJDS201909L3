# -*- coding: UTF-8 -*-

# 定义初始高度
init_height = 100

# 定义初始累加器
sum = 0
sum += init_height
print('No.%2d - Current height=%10f\tSUMMARY=%f' % (1, init_height, sum))

# 定义弹跳次数
times = 20
# 定义第二次弹跳高度与前一次之比
rate = 0.5

next_height = init_height * rate
for n in range(2, times + 1):
    sum += 2 * next_height
    print('No.%2d - Current height=%10f\tSUMMARY=%f' % (n, next_height, sum))
    next_height *= rate

print('\n')
print('Total of road is %f' % sum)
print('The tenth is %f meter' % (next_height/rate))
