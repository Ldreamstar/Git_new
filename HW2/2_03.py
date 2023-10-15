# 渡河问题 农夫0 狼1 羊2 草3
# 初始状态：FFFF 目标状态：TTTT
name = ['farmer', 'wolf', 'sheep', 'grass']
cnt = 0


# 判断是否安全
def safe(sta):
    if sta[1] == sta[2]:
        if sta[0] != sta[2]:
            return False
    if sta[2] == sta[3]:
        if sta[0] != sta[2]:
            return False
    return True


# 判断是否全部通过
def acrossed(sta):
    return sta[0] and sta[1] and sta[2] and sta[3]


# 创建下一个状态的所有情况
def create(sta):
    all_next_sta = []
    for i in range(4):
        if sta[0] == sta[i]:
            next_sta = [sta[0], sta[1], sta[2], sta[3]]
            next_sta[0] = not next_sta[0]
            # 农民通过 ?
            next_sta[i] = next_sta[0]
            # sth和农民一起过

            if safe(next_sta):
                all_next_sta.append(next_sta)
    return all_next_sta


def show(status, riverside):
    result = ""
    for i in range(4):
        if status[i] == riverside:
            if len(result) != 0:
                result += ","
            result += name[i]
    return result


def print_all_history(all_history_status):
    for status in all_history_status:
        print(show(status, False) + "->" + show(status, True))


# 产生方案
def search_step(all_history_sta):
    global cnt
    current_sta = all_history_sta[len(all_history_sta) - 1]
    # 最后一部分历史状态
    all_next_sta = create(current_sta)
    for next_status in all_next_sta:
        if next_status in all_history_sta:
            continue
        # 重复
        all_history_sta.append(next_status)

        if acrossed(next_status):
            cnt += 1
            print("way" + str(cnt) + ":")
            print_all_history(all_history_sta)
        else:
            search_step(all_history_sta)

        all_history_sta.pop()
        # out outside one


status = [False, False, False, False]
all_history_status = [status]
search_step(all_history_status)
