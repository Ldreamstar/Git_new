# 求两个整数的最大公约数

# 遍历法
def gcd1(num1, num2):
    res = 0
    for i in range(2, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            res = i
    print(res)


# 辗转相除法
def gcd2(num1, num2):
    if num1 > num2:
        temp = num1
        num1 = num2
        num2 = temp
    while num2 % num1 != 0:
        tmp = num2 % num1
        num2 = num1
        num1 = tmp
    print(num1)


Num1 = int(input('请输入第一个整数：'))
Num2 = int(input('请输入第二个整数：'))
gcd1(Num1, Num2)
gcd2(Num1, Num2)
