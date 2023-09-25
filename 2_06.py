# 牛顿法求根号c 将起始值g=c/2改为g=c或g=c/4对结果的影响
import math


def square_root1(c):
    initial_guess = c
    i = 0
    precision = 0.00000000001
    while abs(initial_guess * initial_guess - c) > precision:
        initial_guess = (initial_guess + c / initial_guess) / 2
        i += 1
        print("%d:%.13f" % (i, initial_guess))
    print(f'将起始值g=c/2改为g=c共运行{i}次')
    print(f'误差为{abs(initial_guess - math.sqrt(2))}')


square_root1(2)


def square_root2(c):
    initial_guess = c / 4
    i = 0
    precision = 0.00000000001
    while abs(initial_guess * initial_guess - c) > precision:
        initial_guess = (initial_guess + c / initial_guess) / 2
        i += 1
        print("%d:%.13f" % (i, initial_guess))
    print(f'将起始值g=c/2改为g=c/4 共运行{i}次')
    print(f'误差为{abs(initial_guess - math.sqrt(2))}')


square_root2(2)

# 实验结果：将起始值g=c/2改为g=c运行次数不变，改为g=/4运行次数多两次 但是改为c/4精度更高
