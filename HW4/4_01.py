# 判断质数
import math


# 法一：蛮力法:遍历从2到x-1这个区间中的数
def is_prime1(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# 法二：蛮力法:遍历从2到√x即可
def is_prime2(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


# 法三：筛法：从2开始，将2的倍数、3的倍数、4的倍数……都标记为合数，最后没有被标记的数即为素数。
def sieve(n):
    # 初始化一个长度为n+1且内容为True的布尔型数组primes，用来标记每个数是否是素数
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    # 从2开始依次枚举每个数，如果它是素数，则将它的所有倍数都标记为非素数。最后返回所有标记为素数的数。
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def is_prime3(x):
    if x <= 1:
        return False
    primes = sieve(x)
    return primes[x]


a = int(input("请输入一个数字: "))
print(is_prime1(a))
print(is_prime2(a))
print(is_prime3(a))
