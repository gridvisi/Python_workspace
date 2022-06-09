
import numpy as np
import pandas as pd
df = pd.DataFrame({
    "Team": ["A","A","B","B","B",np.nan,np.nan,"C"],
    "Player": [
       "John","Jane","Ashley","Emily","Matt","Jenny","Max","Alex"
    ],
    "Score": [81, 84, np.nan, 91, np.nan, 86, 94, 89]
})
print(df)

print(df["Team"].value_counts())# output
'''
B    3
A    2
C    1
Name: Team, dtype: int64
'''
print(df["Team"].value_counts(dropna=False))# output)

'''
2. 通过使用其他列来填补缺失值
现实生活中的数据集通常包含缺失值，这些缺失值不能总是被忽视。
我们需要适当地处理它们以产生准确和可靠的输出。
我们有不同的选择来填补缺失值。最佳方案取决于数据的特点和任务。
例如，我们可以使用列平均值来填补缺失值。当处理时间序列数据时，
上一个或下一个值可能是一个更好的选择。
另一个选择是使用其他列的数据。在我们的DataFrame中，我们可以
通过使用球员列来填补球队列中的缺失值。我将向你展示这项任务的两
种不同技术。第一个是使用loc方法来手动选择缺失的值。
'''

d = df.loc[df["Team"].isna()==True, "Team"] = df["Player"]
print(d)

df["Team"].fillna(df["Player"], inplace=True)
print(df)

'''
3. 使用Python字典
字典是Python的一个内置数据结构。它在数据分析和操作的各种任务中都很方便。
我们还可以将它们与Pandas函数一起使用，使其更加有用。
例如，替换函数用于替换一列或一个DataFrame中的值。
考虑到我们有一个包含每个球员的球队数据的团队字典。
'''
teams = {
    "John":"A",
    "Jane":"A",
    "Ashley":"B",
    "Emily":"B",
    "Matt":"B",
    "Jenny":"C",
    "Max":"C",
    "Alex":"C"
}

#We can use this dictionary to replace the player names in the team column with their team names.

df["Team"] = df["Team"].replace(teams)
print(df)

df["Team"] = df["Team"].replace("Jenny","C")
df["Team"] = df["Team"].replace("Max","C")

'''
这肯定不如使用字典来得方便。此外，我们可能有几个值要被替换。在这种情况下，与其写几行代码，不如用一个字典只用一行就完成了任务。
你可以用 Python 字典提升其他一些 Pandas 函数。
这里有一篇我写的关于这个主题的更详细的文章。
4个Python Pandas函数用字典更好地服务
更多使用Pandas.havingdatascience.com

4. 有缺失值的整数列
分数列中的数值是整数，但它们被显示为浮点数。原因是这一列中的数值缺失。
整数的默认数据类型不支持空值，所以数据类型被上传到了浮点数。
如果将这些值表示为整数对你来说很重要，你可以使用nullable整数数据类型。
'''

df["Score"] = df["Score"].astype(pd.Int64Dtype())
print(df)