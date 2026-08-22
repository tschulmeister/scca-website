import pandas as pd

df = pd.read_excel('src/data/finances/SCCA_073120.xlsx', header=None)
# Print the whole row where checking is, to see what types of data are in the cells
for i, row in df.iterrows():
    row_str = " ".join([str(x) for x in row if pd.notna(x)])
    if 'Checking' in row_str:
        print(f"Row {i}: {row.values}")
