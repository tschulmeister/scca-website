import pandas as pd

df = pd.read_excel('src/data/finances/SCCA_073120.xlsx', header=None)
print(df.iloc[9:14])
