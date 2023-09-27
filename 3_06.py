# 百分制转等级制

def score_rating(score):
    if score < 60:
        print("你的成绩不合格")
    elif score < 75:
        print("你的成绩合格")
    elif score < 90:
        print("你的成绩良好")
    else:
        print("你的成绩优秀")


my_score = int(input("请输入你的成绩："))
score_rating(my_score)
