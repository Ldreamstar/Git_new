# python开三次方根

# 法一：python内置函数
import math

a = float(input())
res = math.pow(a, 1 / 3)
print(res)

# 法二：幂运算符
a = float(input())
print(a ** (1 / 3))


# 法三：近似思想
def cube_root(num):
    temp = abs(num)
    limit = 0.00001
    low = 0
    high = temp / 2
    while abs(high ** 3 - temp) > limit:
        if high ** 3 > temp:
            high = high - (high - low) / 2
        else:
            high = high + (high - low) / 2
    return high


n = float(input())
if n < 0:
    print('%.5f' % -cube_root(n))
else:
    print('%.5f' % cube_root(n))
