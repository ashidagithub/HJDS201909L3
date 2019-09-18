# -*- coding: UTF-8 -*-

# 定义初始高度
H0 = 100

# 定义初始累加器
SUM = 0
SUM += H0
print('No.%2d - Hn=%10f\tSUM=%f' % (1, H0, SUM))

# 定义弹跳次数
times = 20
# 定义第二次弹跳高度与前一次之比
rate = 0.5

Hn = H0 * rate
for n in range(2, times + 1):
    SUM += 2 * Hn
    print('No.%2d - Hn=%10f\tSUM=%f' % (n, Hn, SUM))
    Hn *= rate

print('\n')
print('Total of road is %f' % SUM)
print('The tenth is %f meter' % (Hn/rate))
