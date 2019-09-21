# -*- coding: UTF-8 -*-

num_start = -100
num_end = 100

for num1 in range(num_start, num_end):
    for num2 in range(num_start, num_end):
        result = num1**2 + num2**2
        if result<=100:
            print('Found: %d^2 + %d^2 = %d' % (num1, num2, result))
