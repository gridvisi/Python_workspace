
# https://towardsdatascience.com/4-python-packages-to-create-interactive-dashboards-d50861d1117e
# 4 Python Packages to Create Interactive Dashboards

# 如何下载数据集 titanic ： https://zhuanlan.zhihu.com/p/266570781
# D:\data_science\dataset
import seaborn as sns
import pandas as pd
#titanic = sns.load_dataset('D:/data_science/dataset/titanic.csv')
titanic = pd.read_csv('D:/data_science/dataset/titanic.csv')
print(titanic.head())


import seaborn as sns
#sns.set_theme(style="darkgrid")

# Load the example Titanic dataset
#df = sns.load_dataset("titanic")

# Make a custom palette with gendered colors
pal = dict(male="#6495ED", female="#F08080")

# Show the survival probability as a function of age and sex
g = sns.lmplot(x="age", y="survived", col="sex", hue="sex", data=df,
               palette=pal, y_jitter=.02, logistic=True, truncate=False)
g.set(xlim=(0, 80), ylim=(-.05, 1.05))