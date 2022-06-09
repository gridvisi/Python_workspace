#https://segmentfault.com/q/1010000017326583
import pandas as pd
df=pd.DataFrame([['The/NOUN'], ['Apple/NOUN'], ['Orange/NOUN']],columns=['words'])
df1=df['words'].str.split('/',expand=True)
df1['size']=df['words'].str.len()
df2=df1[0]+df1['size'].map(lambda x:(26-x)*' ')+df1[1]
print(df2)

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 3
print([s[i:i+n] for i in range(0, len(s), n)])
#['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZ']