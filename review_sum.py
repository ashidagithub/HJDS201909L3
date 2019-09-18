# -*- coding: UTF-8 -*-
import fractions


# -----------------------------
# 自然数列求和
sum = 0
num_start = 1
num_end = 5
for num in range(num_start, num_end + 1):
    sum += num
    print('Add %d to summary, then sum=%d' % (num, sum))

print('Summary of %d-%d is: %d\n' % (num_start, num_end, sum))

# -----------------------------
# 分数列求和
sum = 0
num_start = 1
num_end = 5
for num in range(num_start, num_end + 1):
    fc = fractions.Fraction(1, num)
    sum += fc
    print('Add %s to summary, then sum=%s' % (fc, sum))

print('Summary of 1/%d - 1/%d is: %s\n' % (num_start, num_end, sum))

# -----------------------------
# 等差数列求和
sum = 0
loops = 5

num_start = 1
ap_step = 5  # y=x+5

y = num_start
for idx in range(loops):
    sum += y
    print('Add %d to summary, then sum=%d' % (y, sum))
    y += ap_step

print('Summary is: %d\n' % (sum))

# -----------------------------
# 等比数列求和
sum = 0
loops = 5

num_start = 1
gp_step = 5  # y=x*5

y = num_start
for idx in range(loops):
    sum += y
    print('Add %d to summary, then sum=%d' % (y, sum))
    y *= gp_step

print('Summary is: %d\n' % (sum))

# -----------------------------
# 菲波那切数列求和
sum = 0
loops = 5

a0 = 1
sum += a0
print('Fibonacci sequence (0)= %d, sum=%d' % (a0, sum))

a1 = 2
sum += a1
print('Fibonacci sequence (1)= %d, sum=%d' % (a1, sum))

for idx in range(loops - 2):
    tmp = a1
    a1 += a0
    sum += a1
    print('Fibonacci sequence (%d)= %d, sum=%d' % (idx + 2, a1, sum))
    a0 = tmp
