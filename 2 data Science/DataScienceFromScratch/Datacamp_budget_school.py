
import pandas as pd
df = pd.read_csv("TrainingData.csv",index_col=0)
print(df.info())


# Print the summary statistics
print("____")

import matplotlib.pyplot as plt
#____

# Create the histogram
#____

# Add title and labels
plt.title('Distribution of %full-time \n employee works')
plt.xlabel('% of full-time')
plt.ylabel('num employees')

#print(df.describe())
# Display the histogram
plt.show()

'''
____
              FTE         Total
count  449.000000  1.542000e+03
mean     0.493532  1.446867e+04
std      0.452844  7.916752e+04
min     -0.002369 -1.044084e+06
25%      0.004310  1.108111e+02
50%      0.440000  7.060299e+02
75%      1.000000  5.347760e+03
max      1.047222  1.367500e+06
'''

# Print the summary statistics
print("____")

import matplotlib.pyplot as plt
#____

# Create the histogram
#____

# Add title and labels
plt.title('Distribution of %full-time \n employee works')
plt.xlabel('% of full-time')
plt.ylabel('num employees')
plt.hist(df['FTE'].dropna())
df['FTE'].dropna()
print(df.describe())
# Display the histogram
plt.show()

'''
Nice! The high variance in expenditures makes sense 
(some purchases are cheap some are expensive). 
Also, it looks like the FTE column is bimodal. 
That is, there are some part-time and some full-time employees.

很好! 支出的高差异是有道理的（有些采购很便宜，有些很贵）。
另外，看起来FTE一栏是双模的。也就是说，有一些兼职和一些全职雇员。
'''

'''
将标签编码为分类变量
记住，你的最终目标是预测某个标签被附在预算项目上的概率。你刚才看到，你的数据中的
许多列是低效对象类型。这是否包括你试图预测的标签？让我们来找出答案!

在数据集中有9列标签。每一列都是一个类别，它有许多可能的取值。这9个标签已经被加载
到一个叫做LABELS的列表中。在 Shell 中，使用 df[LABELS].dtypes 检查这些标
签的类型。

你会注意到，每个标签都被编码为一个对象数据类型。因为类别数据类型的效率更高，你的
任务是使用.astype()方法将标签转换为类别类型。

注意：.astype()只在pandas系列中工作。因为你正在使用pandas DataFrame，你
需要使用.apply()方法，并提供一个名为categorize_label的lambda函数，
将.astype()应用于每一列，x。

说明
100 XP
定义lambda函数categorize_label，将列x转换成x.astype('category')。
使用提供的LABELS列表，使用.apply()方法和categorize_label
将数据子集df[LABELS]转换为分类类型。不要忘记 axis=0。
打印df[LABELS]的转换后的.dtypes属性。

接受提示 (-30 XP)
'''

#Q2
'''
# Define the lambda function: categorize_label
categorize_label = lambda ____: ____

# Convert df[LABELS] to a categorical type
df[LABELS] = ____

# Print the converted dtypes
print(____)
'''


# Define the lambda function: categorize_label
categorize_label = lambda x: x.astype('category')

# Convert df[LABELS] to a categorical type
df[LABELS] = df[LABELS].apply(categorize_label,axis=0)

# Print the converted dtypes
print(df[LABELS].dtypes)
'''
    Function            category
    Use                 category
    Sharing             category
    Reporting           category
    Student_Type        category
    Position_Type       category
    Object_Type         category
    Pre_K               category
    Operating_Status    category
    dtype: object
'''

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Calculate number of unique values for each label: num_unique_labels
num_unique_labels = df[LABELS].apply(pd.Series.nunique)

# Plot number of unique values for each label

# Label the axes
plt.xlabel('Labels')
plt.ylabel('Number of unique values')

num_unique_labels.plot()
# Display the plot
plt.show()