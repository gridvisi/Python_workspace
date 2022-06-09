import pandas as pd
#df = pd.read_csv("知乎高赞回答精选80本不同领域圣经级书籍.csv", nrows=10)# Read an Excel spreadsheet
#df = pd.read_excel("知乎高赞回答精选80本不同领域圣经级书籍.xlsx")

# Create a Series from an iterable
integers_s = pd.Series(range(10))# Create a Series from a dictionary object
squares = {x: x*x for x in range(1, 5)}
squares_s = pd.Series(squares)
print(squares)
print(squares_s)

data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
data_df0 = pd.DataFrame(data_dict)
print(data_df0)

# Create a DataFrame from a list
data_list = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
data_df1 = pd.DataFrame(data_list, columns=tuple('abc'))
print(data_df1)

# Find out how many rows and columns the DataFrame has
df.shape


'''

# Take a quick peak at the beginning and the end of the data
df.head()
df.tail()# Get a random sample
df.sample(5)# Get the information of the dataset
df.info()# Get the descriptive stats of the numeric values
df.describe()
'''
