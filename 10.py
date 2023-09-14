# 判断字符串是否由两个或以上连续的相同字符组成的

# 法一:使用字符串计数器
S = input('请输入一个字符串：')
Num = 0
for Str in S:
    if S.count(Str) > 0:
        Num += 1
if Num > 0:
    print('Yes!')
else:
    print('No!')

# 法二:遍历
S = input('请输入一个字符串：')
i = 0
for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        break
if i < len(S) - 2 or S[i] == S[i + 1]:
    print('Yes!')
else:
    print('No!')

# 法三：简单粗暴法
S = input('请输入一个字符串：')
Set = set()
flag = 0
for Str in S:
    if Str in Set:
        print('Yes!')
        flag = 1
        break
    Set.add(Str)
if flag == 0:
    print('No!')
