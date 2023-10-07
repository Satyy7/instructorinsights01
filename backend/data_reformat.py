import pandas as pd
import numpy as np

df = pd.read_csv('./csv/professors.csv')

# Convert rating count to integer
df['Rating Count'] = df['Rating Count'].str.split(" ").str[0]
df['Rating Count'] = df['Rating Count'].astype(int)
# print(df.dtypes)

#Convert WTA % to int
df['Would Take Again %'] = df['Would Take Again %'].str.strip('%')
df['Would Take Again %'] = pd.to_numeric(df['Would Take Again %'], errors='coerce') ## ignores null values
# print(df.dtypes)

df.to_csv('./csv/cleaned_data.csv',index=False)

