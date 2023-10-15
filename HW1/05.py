x = int(input("x的值为："))
y = int(input("y的值为："))
z = int(input("z的值为："))
# 始终保证x小于y
if x > y:
    x, y = y, x

if x > z:
    print(f'从小到大排序后为{z} {x} {y}')
elif y > z:
    print(f'从小到大排序后为{x} {z} {y}')
else:
    print(f'从小到大排序后为{x} {y} {z}')
