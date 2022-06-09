#https://zhuanlan.zhihu.com/p/96040773?from_voters_page=true
import seaborn as sns
#%matplotlib inline
sns.set(font_scale=1.5)
flights = sns.load_dataset("flights")
flights.head()

'''
#导入数据集后按年月两个维度进行数据透视
data=sns.load_dataset("flights")\
        .pivot("month","year","passengers")
data.head()
'''