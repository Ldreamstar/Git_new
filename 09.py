# for循环实现给定数列的倒排序
# L = [1, 2, 3, 4, 5]
L = input('请输入一个列表:')
L = eval(L)
# print(type(L)) eval将字符串类型转换为列表
res_list = []
for i in L:
    res_list.append(i)
res_list = sorted(res_list, reverse=True)
print(res_list)

# while循环实现给定数列的倒排序
L = input('请输入一个列表:')
L = eval(L)
res_list = []
i = 0
while i < len(L):
    res_list.append(L[i])
    i += 1
res_list = sorted(res_list, reverse=True)
print(res_list)
