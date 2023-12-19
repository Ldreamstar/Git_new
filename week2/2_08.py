# 基于python求解圆周率的值
import random
import math


# 法一：蒙特卡罗法
def calculate_pi_throw(precision):
    cnt = 10000
    pi = 0
    while abs(pi - math.pi) > precision:
        cirtle = 0
        out_cirtle = 0
        i = 0
        while i < cnt:
            i += 1
            x = random.random()
            y = random.random()
            if (x * x + y * y) < 1:
                cirtle += 1
            else:
                out_cirtle += 1
        cnt += 1
        pi = 4 * (cirtle / 1.0) / (out_cirtle + cirtle)
    print("蒙特卡罗法的结果为%.10f,需要迭代%d步" % (pi, cnt))
    return


calculate_pi_throw(0.0001)


# 法二：leibniz 级数方法， π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
def calculate_pi_leibniz(precision):
    pi = 0
    i = 0
    while abs(4 * pi - math.pi) > precision:
        numerator = (-1) ** i
        denominator = 2 * i + 1
        pi += numerator / denominator
        i += 1
    print("leibniz级数法的结果为%.10f,需要迭代%d步" % (4 * pi, i))
    return


calculate_pi_leibniz(0.00001)


# 法三：Nilakantha Somayaji级数 π = 3 + 4 / (234) - 4 / (456) + 4 / (678) - 4 / (8910) + 4 / (101112) - ...
def calculate_pi_nilakantha(precision):
    pi = 3.0
    sign = 1  # 用于交替加减
    denominator = 2
    i = 0
    while abs(pi - math.pi) > precision:
        pi += sign * (4.0 / (denominator * (denominator + 1) * (denominator + 2)))
        sign *= -1
        denominator += 2
        i += 1
    print("Nilakantha级数法的结果为%.10f,需要迭代%d步" % (pi, i))
    return


calculate_pi_nilakantha(0.00000000001)


