def max_multi(Num, a):
    if Num == 1 or Num == 2 or Num == 3:
        a.append(Num)
        return
    elif Num == 4:
        a.append(2)
        a.append(2)
        return
    else:
        a.append(3)
        max_multi(Num - 3, a)


num = int(input("请输入一个整数： "))
alist = []
max_multi(num, alist)
alist.sort()
print("所求得的正整数列表为：")
print(alist)
