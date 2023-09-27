import pandas as pd
df = pd.read_csv ('file_name.csv')
print(df)
new_df = pd.read_csv('file_name.csv', usecols= ['column_name1','column_name2'])
print(new_df)

