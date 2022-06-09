
#16

import datetime
import dateutil.parser
input_date = '04th Dec 2020'
parsed_date = dateutil.parser.parse(input_date)

op_date = datetime.datetime.strftime(parsed_date, '%Y-%m-%d')
print(op_date)


# 17. Invert a Dictionary
l_dict = {'Person_Name':'Naina',
           'Age' : 27,
           'Profession' : 'Software Engineer'
           }
invert_dict = {values:keys for keys,values in l_dict.items()}
print(invert_dict)


#18. Pretty Dictionaries
l_dict = {'Student_ID': 4,'Student_name' : 'Naina', 'Class_Name': '12th' ,'Student_marks' : {'maths' : 92,
                            'science' : 95,
                            'computer science' : 100,
                            'English' : 91}
          }

import pprint
pprint.pprint(l_dict)

# 19. Convert List of list to list
import itertools

nested_list = [['Naina'], ['Alex', 'Rhody'], ['Sharron', 'Avarto', 'Grace']]
converted_list = list(itertools.chain.from_iterable(nested_list))
print(converted_list)


#20. Removing Emojis from Text
Emoji_text = 'For example, 🤓🏃‍🏢 could mean “Iam running to work.”'
final_text= Emoji_text.encode('ascii', 'ignore').decode('ascii')
print("Raw tweet with Emoji:",Emoji_text)
print("Final tweet withput Emoji:",final_text)


'''
21. 并行应用Pandas操作
它用于将你的pandas计算分布在你电脑上所有可用的CPU上，以获得速度上的显著提高。
安装pandarallel :
'''
# pip install pandarallel

#%load_ext autoreload
#%autoreload 2
import pandas as pd
import time
from pandarallel import pandarallel
import math
import numpy as np
import random
#from tqdm._tqdm_notebook import tqdm_notebook
from pandas import Panel

# FutureWarning: The Panel class is removed from pandas.
# Accessing it from the top-level namespace will also be removed in
# the next version
#tqdm_notebook.pandas()

pandarallel.initialize(progress_bar=True)
df = pd.DataFrame({
    'A' : [random.randint(8,15) for i in range(1,100000) ],
    'B' : [random.randint(10,20) for i in range(1,100000) ]
})

def trigono(x):
    return math.sin(x.A**2) + math.sin(x.B**2) + math.tan(x.A**2)

#%%time
first = df.progress_apply(trigono, axis=1)

#%%time
first_parallel = df.parallel_apply(trigono, axis=1)

# 22. Pandas Cut and qcut
'''
在Pandas中。
cut命令创建等间距的bin，但每个bin中的样本频率是不相等的。
qcut命令创建不等大小的仓，但每个仓中的样本频率是相等的。
导入必要的库。
'''

import pandas as pd
import numpy as np
df_rollno = pd.DataFrame({'Roll No': np.random.randint(20, 55, 10)})
print(df_rollno)

df_rollno['roll_no_bins'] = pd.cut(x=df_rollno['Roll No'], bins=[20, 40, 50, 60])
print(df_rollno)


pd.qcut(df_rollno['Roll No'], q=6)
print(df_rollno)

# 23. Pandas Profiling
'''

It’s used to generates profile reports from a pandas DataFrame or data sheet.
Install Pandas Profiling:

它用于从pandas DataFrame或数据表中生成分析报告。
安装Pandas Profiling
pip install pandas-profiling
'''
# D:\data_science\csvTraining
# https://zhuanlan.zhihu.com/p/85967505

import pandas as pd
import pandas_profiling
Youtube_data = pd.read_csv('d:/data_science/csvTraining.csv')