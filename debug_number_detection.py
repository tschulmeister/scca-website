import pandas as pd
import numpy as np

df = pd.read_excel('src/data/finances/SCCA_073120.xlsx', header=None)

def is_number(val):
    return isinstance(val, (int, float, np.float64, np.int64)) and not np.isnan(val)

# ... testing my logic
for i, row in df.iterrows():
    row_str = " ".join([str(x) for x in row if pd.notna(x)])
    if 'Checking' in row_str:
        print(f"Row {i} found: {row.values}")
        for cell in row:
            if is_number(cell):
                print(f"Found number: {cell}")
