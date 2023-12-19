import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
iris_data = iris.data
iris_labels = iris.target
iris_feature_names = iris.feature_names

iris_df = pd.DataFrame(data=iris_data, columns=iris_feature_names)
iris_df['Species'] = iris_labels

sns.set(style="whitegrid")

# 散点图 Pairplot
sns.pairplot(iris_df, hue="Species", markers=["o", "s", "D"])
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.show()

# 箱线图 Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x="Species", y="sepal length (cm)", data=iris_df)
plt.title("Boxplot of Sepal Length by Species")
plt.show()

# 直方图 Histogram
plt.figure(figsize=(10, 6))
sns.histplot(iris_df, x="petal length (cm)", hue="Species",
             element="step", stat="density", common_norm=False)
plt.title("Histogram of Petal Length by Species")
plt.show()
