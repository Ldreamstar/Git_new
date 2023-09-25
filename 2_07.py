def cube_root_newton(c, initial_guess):
    x = initial_guess
    precision = 1e-6

    i = 0
    while abs(x ** 3 - c) > precision:
        f_x = x ** 3 - c
        f_prime_x = 3 * x ** 2
        x -= f_x / f_prime_x
        i += 1
        print("%d:%.13f" % (i, x))


cube_root_newton(10, 1)  # 使用1作为初始猜测值
