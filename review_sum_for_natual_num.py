# -*- coding: UTF-8 -*-

n = 100
Sn = 0

for num in range(1, n+1):
    Sn += num
    print('Loops at %d, summary=%d' %(num, Sn))

print(Sn)
