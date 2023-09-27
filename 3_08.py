# 随机生成多组长度递增的随机数列，使用不同排序算法对这些数列的数据排序，分析不同排序算法在不同长度数列下的运行效果
import random
import time
import copy

list1 = []
list2 = []
list3 = []
list4 = []
data_list = [list1, list2, list3, list4]
len_list = [100, 1000, 10000]

for i in range(3):
    for _ in range(len_list[i]):
        data_list[i].append(random.uniform(0, 10000))

# 使用copy.deepcopy创建data_list1的独立副本
data_list1 = copy.deepcopy(data_list)


# 选择排序算法
def selection_sort(q_list):
    for j in range(len(q_list)):
        min_idx = j
        for k in range(j + 1, len(q_list)):
            if q_list[k] < q_list[min_idx]:
                min_idx = k
        q_list[min_idx], q_list[j] = q_list[j], q_list[min_idx]


# 归并排序算法
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(q_list):
    if len(q_list) <= 1:
        return q_list
    mid = len(q_list) // 2
    left = merge_sort(q_list[:mid])
    right = merge_sort(q_list[mid:])
    return merge(left, right)


time1 = []
time2 = []

for i in range(3):
    start_time = time.time()
    selection_sort(data_list[i])
    end_time = time.time()
    time1.append(end_time - start_time)

for i in range(3):
    start_time = time.time()
    data_list1[i] = merge_sort(data_list1[i])
    end_time = time.time()
    time2.append(end_time - start_time)

print(f'使用选择排序对3组长度递增的随机数列排序所用时间列表为{time1}')
print(f'使用归并排序对3组长度递增的随机数列排序所用时间列表为{time2}')

