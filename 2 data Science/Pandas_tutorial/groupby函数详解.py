'''
https://blog.csdn.net/weixin_42782150/article/details/90716533?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.add_param_isCf&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.add_param_isCf
'''

import numpy as np
import pandas as pd
df=pd.DataFrame({'key1':['a','a','b','b','a'],
                 'key2':['one','two','one','two','one'],
                  'data1':np.random.randn(5),
                  'data2':np.random.randn(5)})
#'key1':['a','a','b','b','a']亦可写作'key1':list('aabba'),完成列表的创建
'''
df
   key1	 key2	    data1	  data2
0	a	 one	  -0.484689	  -3.105627
1	a	 two	  0.033929	  1.182974
2	b	 one	  1.067201	  -1.707349
3	b	 two	  -0.960876	  -0.190247
4	a	 one	  0.305254	  0.322322
#（1）按指定的某一列进行聚合
'''
for i in df.groupby('key1'):
    print(i)
'''
>>>
('a',   key1   key2     data1      data2
0        a     one     -0.484689   -3.105627
1        a     two     0.033929    1.182974
4        a     one     0.305254    0.322322)
('b',   key1   key2     data1      data2
2        b     one     1.067201    -1.707349
3        b     two     -0.960876   -0.190247)
#（2）按多列进行聚合，新的DataFrame是多列之间维度的笛卡尔积

'''
for i in df.groupby(['key1','key2']):
    print(i)
'''
>>>
(('a', 'one'),   key1    key2     data1      data2
      0          a       one      -0.484689  -3.105627
      4          a       one      0.305254   0.322322)
(('a', 'two'),   key1    key2     data1     data2
      1          a       two      0.033929   1.182974)
(('b', 'one'),   key1    key2     data1     data2
      2          b       one      1.067201 -1.707349)
(('b', 'two'),   key1   key2     data1     data2
      3          b       two      -0.960876 -0.190247)
#（3） 按key1进行分组，并计算data1列的平均值

'''
df1=df['data1'].groupby(df['key1']).mean()
'''
>>>
key1
a       -0.048502
b       0.053162
#（4） 按key1、key2进行分组，并计算data1列的平均值,聚合表不堆叠
#将数据从“花括号”格式转为“表格”格式，unstack即“不要堆叠”

'''
df2=df['data1'].groupby([df['key1'],df['key2']]).mean().unstack()
'''
>>>df2
key2	one	        two
key1		
a	    -0.089718	 0.033929
b	    1.067201	 -0.960876

'''
#(5)分组键可以是与原df无关的，另外指定的任何长度适当的数组，新数组按列表顺序分别与df[col_1]的数据一一对应。
states=np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years=np.array([2004,2005,2006,2005,2006])
df['data1'].groupby([states,years]).mean()
'''
>>>
California  2005    0.033929
            2006    1.067201
Ohio        2004   -0.484689
            2005   -0.960876
            2006    0.305254
#用到GroupBy的size方法，它可以返回一个含有分组大小的Series
'''
df.groupby(['key1','key2']).size()
'''
>>>
      key1  key2
a     one     2
      two     1
b     one     1
      two     1

'''