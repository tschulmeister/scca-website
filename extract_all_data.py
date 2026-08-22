import pandas as pd
import os
import re
import numpy as np
import json

def is_number(val):
    return isinstance(val, (int, float, np.float64, np.int64)) and not np.isnan(val)

def extract_financials(filepath):
    df = pd.read_excel(filepath, header=None)
    
    data = {
        'checking': None,
        'money_market': None,
        'total_funds': None
    }
    
    # Try to find the date from the filename or the first few rows
    date_match = re.search(r'(\d{6,8})', os.path.basename(filepath))
    if date_match:
        data['date'] = date_match.group(1)
    else:
        data['date'] = None

    for i, row in df.iterrows():
        # Clean the row to search easily
        row_str = " ".join([str(x) for x in row if pd.notna(x)])
        
        if 'Checking' in row_str:
            for cell in row:
                if is_number(cell):
                    data['checking'] = float(cell)
                    break
        elif 'Money Market' in row_str or 'CD' in row_str:
            for cell in row:
                if is_number(cell):
                    data['money_market'] = float(cell)
                    break
        elif 'Total' in row_str and 'Funds' in row_str:
            for cell in row:
                if is_number(cell):
                    data['total_funds'] = float(cell)
                    break
                    
    return data

results = []
folder = 'src/data/finances'
for file in os.listdir(folder):
    if file.endswith(('.xlsx', '.xlsb')):
        try:
            res = extract_financials(os.path.join(folder, file))
            res['file'] = file
            results.append(res)
        except Exception as e:
            print(f"Failed {file}: {e}")

print(json.dumps(results, indent=2))
