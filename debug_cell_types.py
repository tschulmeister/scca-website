import pandas as pd

df = pd.read_excel('src/data/finances/SCCA_073120.xlsx', header=None)

# Print types of all items in row 10
print(f"Row 10 values: {df.iloc[10].values}")
for val in df.iloc[10]:
    print(f"Value: {val}, Type: {type(val)}")
