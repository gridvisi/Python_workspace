# https://stackoverflow.com/questions/70111200/pandas-dataframe-median-of-a-column-with-condition

import pandas as pd

# Build dataframe
data = [['Paris', 2], ['New York', 3], ['Rome', 4], ['Paris', 5], ['Paris', 4]]
df = pd.DataFrame(data, columns=['location', 'price'])

# Get paris only rows
df_paris = df[df['location'] == 'Paris']

# Print median
print(df_paris['price'].median())