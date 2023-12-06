import matplotlib
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(0, 12.1, 0.1)  # 每0.1一个点从0一直建到12
Y = np.sin(X)

plt.plot(X, Y)
