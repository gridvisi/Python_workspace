#https://morioh.com/p/3b5a82ac43e6?f=5c21fb01c16e2556b555ab32


#3. copy This is an important command if you haven’t heard of it already. If you do the following commands:

import pandas as pd
df1 = pd.DataFrame({ 'a':[0,0,0], 'b': [1,1,1]})
df2 = df1
df2['a'] = df2['a'] + 1
df1.head()
print(df1)
print(df2)

#copy
df2 = df1.copy()
from copy import deepcopy
df2 = deepcopy(df1)

level_map = {1: 'high', 2: 'medium', 3: 'low'}
#df['c_level'] = df['c'].map(level_map)

#5. apply or not apply?If we’d like to create a new column with a few other columns as inputs,
#apply function would be quite useful sometimes.

def rule(x, y):
    if x == 'high' and y > 10:
         return 1
    else:
         return 0

df = pd.DataFrame({ 'c1':[ 'high' ,'high', 'low', 'low'], 'c2': [0, 23, 17, 4]})
df['new'] = df.apply(lambda x: rule(x['c1'], x['c2']), axis =  1)
df.head()
print(df)

df['maximum'] = df.apply(lambda x: max(x['c2'], x['c2']), axis = 1)
#but you’ll find it much slower than this command:
df['maximum'] = df[['c1','c2']].max(axis =1)
print(df)

'''
6. value counts
This is a command to check value distributions. For example, if you’d like to check 
what are the possible values and the frequency for each individual value in column ‘c’ you can do

df['c'].value_counts()

There’re some useful tricks / arguments of it:
A. normalize = True: if you want to check the frequency instead of counts.
B. dropna = False: if you also want to include missing values in the stats.
C. df['c'].value_counts().reset_index(): if you want to convert the stats table into a pandas 
dataframe and manipulate it
D. df['c'].value_counts().reset_index().sort_values(by='index') : 
show the stats sorted by distinct values in column ‘c’ instead of counts.

7. number of missing values
When building models, you might want to exclude the row with too many missing 
values / the rows with all missing values. You can use .isnull() and .
sum() to count the number of missing values within the specified columns.
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({ 'id': [1,2,3], 'c1':[0,0,np.nan], 'c2': [np.nan,1,1]})
df = df[['id', 'c1', 'c2']]
df['num_nulls'] = df[['c1', 'c2']].isnull().sum(axis=1)
df.head()
print(df)

'''
8. select rows with specific IDs
In SQL we can do this using SELECT * FROM … WHERE ID in (‘A001’, ‘C022’, …) to get records with specific IDs. If you want to do the same thing with pandas, you can do

df_filter = df['ID'].isin(['A001','C022',...])
df[df_filter]

9. Percentile groups
You have a numerical column, and would like to classify the values in that column into groups, say top 5% into group 1, 5–20% into group 2, 20%-50% into group 3, bottom 50% into group 4. Of course, you can do it with pandas.cut, but I’d like to provide another option here:

which is fast to run (no apply function used).
'''
import numpy as np
cut_points = [np.percentile(df['c'], i) for i in [50, 80, 95]]
df['group'] = 1
for i in range(3):
    df['group'] = df['group'] + (df['c'] < cut_points[i])
# or <= cut_points[i]
print(df)

'''
10. to_csv
Again this is a command that everyone would use. I’d like to point out two tricks here. The first one is

print(df[:5].to_csv())

You can use this command to print out the first five rows of what are going to be written into 
the file exactly.

Another trick is dealing with integers and missing values mixed together. If a column contains 
both missing values and integers, the data type would still be float instead of int. 
When you export the table, you can add float_format=‘%.0f’ to round all the floats to integers. 
Use this trick if you only want integer outputs for all columns — you’ll get rid of all annoying ‘.0’s.

Thanks for reading ❤

If you liked this post, share it with all of your programming buddies!

Welcome to Morioh!
Morioh is the place to create a Great Personal Brand, connect with Developers around the
World and grow your Career! Let's write, share knowledge and earn GeekCash.

React JS - A Complete Guide for Frontend Web Development
13,888 students enrolled

Python Pandas Tutorial (Part 1): Getting Started with Data Analysis
Python Pandas Tutorial (Part 9): Cleaning Data - Casting Datatypes ...
Python Pandas Tutorial (Part 2): 

'''