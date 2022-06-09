
import blackfriday
print(blackfriday)

#首先还是最基础的先导入各个可能会使用到的库
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline

#下面开始导入数据 #在这里我使用r来使得read_csv可以使用
df = pd.read_csv(r"C:\Users\Administrator\Desktop\From Zero To Hero\BlackFriday.csv")

'''
df.info() 
#运行结果 
<class 'pandas.core.frame.DataFrame'> RangeIndex: 537577 entries,
 0 to 537576 Data columns (total 12 columns): 
User_ID                       537577 non-null int64 
Product_ID                    537577 non-null object 
Gender                        537577 non-null object 
Age                           537577 non-null object 
Occupation                    537577 non-null int64 
City_Category                 537577 non-null object 
Stay_In_Current_City_Years    537577 non-null object 
Marital_Status                537577 non-null int64 
Product_Category_1            537577 non-null int64 
Product_Category_2            370591 non-null float64 
Product_Category_3            164278 non-null float64 
Purchase                      537577 non-null int64 
dtypes: float64(2), int64(5), object(5) 
memory usage: 49.2+ MB 
'''

'''
#看一下表格的前10行，从整体上了解基本信息 df.head(10)

User_ID	Product_ID	Gender	Age	Occupation	City_Category	Stay_In_Current_City_Years	Marital_Status	Product_Category_1	Product_Category_2	Product_Category_3	Purchase
0	1000001	P00069042	F	0-17	10	A	2	0	3	NaN	NaN	8370
1	1000001	P00248942	F	0-17	10	A	2	0	1	6.0	14.0	15200
2	1000001	P00087842	F	0-17	10	A	2	0	12	NaN	NaN	1422
3	1000001	P00085442	F	0-17	10	A	2	0	12	14.0	NaN	1057
4	1000002	P00285442	M	55+	16	C	4+	0	8	NaN	NaN	7969
5	1000003	P00193542	M	26-35	15	A	3	0	1	2.0	NaN	15227
6	1000004	P00184942	M	46-50	7	B	2	1	1	8.0	17.0	19215
7	1000004	P00346142	M	46-50	7	B	2	1	1	15.0	NaN	15854
8	1000004	P0097242	M	46-50	7	B	2	1	1	16.0	NaN	15686
9	1000005	P00274942	M	26-35	20	A	1	1	8	NaN	NaN	7871
'''
