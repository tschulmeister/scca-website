import pandas as pd
import os

folder_path = 'src/data/finances'
files = [f for f in os.listdir(folder_path) if f.endswith(('.xlsx', '.xlsb'))]

for file in files:
    try:
        # Some files might be xlsb, pandas can't always read them directly with openpyxl
        # but let's try standard excel reading first
        df = pd.read_excel(os.path.join(folder_path, file))
        print(f"--- {file} ---")
        print(df.head())
        print("\n")
    except Exception as e:
        print(f"--- {file} ---")
        print(f"Error reading: {e}")
        print("\n")
