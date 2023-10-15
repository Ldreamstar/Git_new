w = int(input("w的值为："))
x = int(input("x的值为："))
y = int(input("y的值为："))
z = int(input("z的值为："))

my_list = [w, x, y, z]
res_list = sorted(my_list, reverse=True)
print(*res_list)
# print函数调用中使用*操作符，可以将列表中的元素作为独立的参数传递给print函数。这样，列表的方括号将不会出现在输出中。
