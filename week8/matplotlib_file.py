import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()
data = iris.data
target = iris.target
feature_names = iris.feature_names

# 散点图
plt.figure(figsize=(12, 6))
for i in range(3):
    plt.scatter(data[target == i, 0], data[target == i, 1], label=f'Class {i}')
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.title('Scatter Plot of Iris Dataset')
plt.legend()
plt.show()

# 箱线图
plt.figure(figsize=(8, 6))
plt.boxplot([data[target == i, 2] for i in range(3)],
            labels=[f'Class {i}' for i in range(3)])
plt.xlabel('Classes')
plt.ylabel(feature_names[2])
plt.title('Box Plot of Sepal Length by Class')
plt.show()

# 直方图
plt.figure(figsize=(8, 6))
for i in range(3):
    plt.hist(data[target == i, 3], bins=20, alpha=0.5, label=f'Class {i}')
plt.xlabel(feature_names[3])
plt.ylabel('Frequency')
plt.title('Histogram of Petal Width by Class')
plt.legend()
plt.show()