import random
import math
import numpy as np


# 法一：概率论
# 定义被积函数
def f(x):
    return x ** 2 + 4 * x * math.sin(x)


# 指定积分区间
a = 2
b = 3

# 生成随机样本点数量
num_samples = 100000

# 统计下方点数量
under_curve = 0

# 随机生成样本点统计下方点数量
for _ in range(num_samples):
    x = random.uniform(a, b)  # random.uniform用于生成一个[a,b]内的随机浮点数。
    y = random.uniform(0, max(f(x) for x in [a, b]))  # 在函数值范围内生成随机点
    if y <= f(x):
        under_curve += 1

# 估算定积分
integral_estimate = (b - a) * (max(f(x) for x in [a, b])) * (under_curve / num_samples)
print("%.6f" % integral_estimate)


# 法二：定积分的几何意义
def Monte_Carlo_Method(a, b):
    # (a,b)是积分区间
    x = np.random.uniform(a, b, 1000000)
    result = 0
    for i in x:
        result += f(i)

    return result / 1000000


final = Monte_Carlo_Method(2, 3)
print("%.6f" % final)
