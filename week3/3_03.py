# 用正则表达式验证身份证号是否合法

import re


def is_valid_identity(identity):
    pattern = re.compile(r'^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$')
    return pattern.match(identity)


identity_card = input("请输入身份证号码：")
print(is_valid_identity(identity_card))

# 地区： [1-9]\d{5}
# 年的前两位： (18|19|([23]\d)) 1800-2399
# 年的后两位： \d{2}
# 月份： ((0[1-9])|(10|11|12))
# 天数： (([0-2][1-9])|10|20|30|31) 闰年不能禁止29+
# 三位顺序码： \d{3}
# 两位顺序码： \d{2}
# 校验码： [0-9Xx]
