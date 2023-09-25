# 牛顿法求根号c
import math


def square_root(c):
    initial_guess = c / 2
    i = 0
    precision = 0.00000000001
    while abs(initial_guess * initial_guess - c) > precision:
        initial_guess = (initial_guess + c / initial_guess) / 2
        i += 1
        print("%d:%.13f" % (i, initial_guess))
    print(f'求解根号{c}的起始值为g=c/2共运行{i}次')
    print(f'误差为{abs(initial_guess - math.sqrt(2))}')


square_root(2)
square_root(2000)
