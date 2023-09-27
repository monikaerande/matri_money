# import os
# if os.path.exists("C:\\Users\\HP G5\\OneDrive\\Desktop\\test.txt"):
#     print("path exist")
#     os.remove("C:\\Users\\HP G5\\OneDrive\\Desktop\\test.txt")
#     print("file removed")
# else:
#     print("path not exist")

#
# import os
# os.rmdir("C:\\Users\\HP G5\\OneDrive\\Desktop\\aaa")


import pandas as pd
df = pd.read_csv ('file_name.csv')
print(df)
new_df = pd.read_csv('file_name.csv', usecols= ['column_name1','column_name2'])
print(new_df)

#changes by akshay

