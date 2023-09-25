# 笨办法求解根号c(2)

def square_root():
    c = 2
    i = 0  # 迭代次数
    g = 0
    precision = 0.0001
    for j in range(c):
        if j * j > c and g == 0:
            g = j - 1
    while abs(g * g - c) > precision:
        g += 0.00001
        i = i + 1
        print("%d:g=%.5f" % (i, g))


square_root()
