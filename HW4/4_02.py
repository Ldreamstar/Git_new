# 利用python获取程序执行时间
import time
import datetime

# 法一
start = time.perf_counter()
list_ = [x for x in range(0, 1000000, 2)]
end = time.perf_counter()
print(f"时间开销：{end - start}")

# 法二
start1 = time.time()
list1 = [x for x in range(0, 1000000, 2)]
end1 = time.time()
print(f"时间开销：{end1 - start1}")

# 法三
start2 = datetime.datetime.now()
list2 = [x for x in range(0, 1000000, 2)]
end2 = datetime.datetime.now()
print(f"时间开销：{end2 - start2}")
