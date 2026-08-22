import pandas as pd
import os

# Let's look further down into a file to see where the actual data starts.
# Most look like they have a header and then data.

def inspect_file(filename):
    print(f"--- Inspecting {filename} ---")
    df = pd.read_excel(os.path.join('src/data/finances', filename))
    # Show first 20 rows to identify headers
    print(df.iloc[0:30])

inspect_file('SCCA_073120.xlsx')
