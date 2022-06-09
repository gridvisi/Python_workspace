import pandas as df
import seaborn as sns
import matplotlib.pyplot as plt
# heat map for correlation coefficient
# https://seaborn.pydata.org/

sns.heatmap(df.core(), annot=True, fmt="0.2")

#plotting the time series analysis with a red regression line
sns.regplot(data=df, x="Variable_1", y="Variable_2", line_kws={"color": "red"})
plt.xlabel('Variable 1', size=14)
plt.ylabel('Variable 2', size=14)
plt.title('(LINEAR) REGRESSION BETWEEN TWO VARIABLES')