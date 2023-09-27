# 完成十到二进制小数的转换

def decimal_to_binary(decimal_num, num_places=8):
    binary_num = ""

    # 处理小数点之前的部分
    integer_part = int(decimal_num)
    binary_num += bin(integer_part)[2:]  # bin将十进制转化为二进制（字符串形式），切片去掉二进制字符串前面的"0b"

    # 处理小数点
    binary_num += "."

    # 处理小数点之后的部分：乘2取整
    fractional_part = decimal_num - integer_part
    for _ in range(num_places):
        fractional_part *= 2
        binary_digit = int(fractional_part)
        binary_num += str(binary_digit)
        fractional_part -= binary_digit

    return binary_num


decimal_number = float(input("请输入一个十进制数字："))
binary_result = decimal_to_binary(decimal_number)
print(f"{decimal_number} 的二进制表示为：{binary_result}")
