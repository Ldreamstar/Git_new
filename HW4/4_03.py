# 分析插入排序的流程
L = []
n = int(input("请输入列表的数据规模："))
for i in range(n):
    x = float(input("请输入列表数字"))
    L.append(x)

for i in range(1, len(L)):
    for j in range(i - 1, -1, -1):
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
    print(L)
