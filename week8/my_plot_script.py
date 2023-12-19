import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 线图
X = np.arange(0, 12.1, 0.1)  # 每0.1一个点从0一直建到12
Y = np.sin(X)

plt.plot(X, Y, color='lime', linestyle='', linewidth=2, \
         marker='v', markerfacecolor='black', markeredgecolor='red', \
         markersize=4, markeredgewidth=1, label='Normal case', zorder=1)
# plt.scatter(X,Y)

ax1 = plt.gca()
ax1.set_title('Big Title', fontname='Arial', fontsize=20, \
              weight='bold', style='italic')
ax1.set_xlabel('time (UTC)')
# ax1.set_ylabel('T ($^o$C)')
ax1.set_ylabel('T ($\mu$C)')

# 刻度
ax1.set_xticks([0, 2.5, 7, 11])
# 刻度标签设置
ax1.set_xticklabels(['J', 'A', 'N', 'E'])
# 设置刻度的方向
ax1.tick_params(axis='both', direction='in', color='blue', length=10, width=2)

# 同一图中画多条线
plt.plot(X + 2, Y, label='Strange', linewidth=4, zorder=2)

# 设置图例位置 best/lower left/upper right
plt.legend(loc='best')

# 设置图层顺序 plt.plot(...,zorder=#) zorder用来控制绘图顺序，其值越大，画上去越晚，线条的叠加就是在上面的

# 子图绘制
fig, ax = plt.subplots(2, 1)
ax[1].plot(X, Y)
ax[0].plot(X + 2, Y, 'r')
# 设置坐标轴范围
ax[1].set_xlim([0, 10])
ax[0].set_xlim([0, 10])

X2 = np.arange(1, 100, 1)
Y2 = np.exp(X2)
plt.plot(X2, Y2)
plt.ylim([1, 10000])  # 调整Y轴范围
ax2 = plt.gca()
# 设置指数坐标轴
ax2.set_yscale('log')

# 设置双坐标轴
ax2 = ax[1].twinx()
ax2.plot(X, Y, 'ro')  # 'ro' 表示红色（'r'）的圆点（'o'）

ax3 = ax[1].twiny()
ax3.plot(X, Y, 'ro')

plt.show()
