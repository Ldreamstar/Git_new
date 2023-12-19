input_string = input("请输入一个空格分隔的数字列表: ")

# 使用split()函数将输入的字符串分割成数字字符串的列表
number_strings = input_string.split()

# 将数字字符串列表转换为整数列表
A = [int(num) for num in number_strings]

B = []

for i in range(len(A)):
    res = 1
    for j in range(len(A)):
        if j != i:
            res *= A[j]
    B.append(res)
print(B)
