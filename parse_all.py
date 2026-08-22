import pandas as pd
import os
import re

def extract_financials(filepath):
    df = pd.read_excel(filepath, header=None)
    
    # We are looking for numeric values. Sometimes they are in column 4, 5, or 6
    # Let's iterate and look for keywords, then look at adjacent columns
    
    extracted = {
        'date': None,
        'checking': None,
        'money_market': None,
        'total_funds': None
    }
    
    # Try to find the date from the filename or the first few rows
    date_match = re.search(r'(\d{6,8})', filepath)
    if date_match:
        extracted['date'] = date_match.group(1)
        
    for i, row in df.iterrows():
        row_str = " ".join([str(x) for x in row if pd.notna(x)])
        
        if 'Checking' in row_str:
            # find the first numeric value in this row
            for cell in row:
                if isinstance(cell, (int, float)):
                    extracted['checking'] = cell
                    break
        elif 'Money Market' in row_str:
            for cell in row:
                if isinstance(cell, (int, float)):
                    extracted['money_market'] = cell
                    break
        elif 'Total Funds' in row_str:
            for cell in row:
                if isinstance(cell, (int, float)):
                    extracted['total_funds'] = cell
                    break
                    
    return extracted

data = []
folder = 'src/data/finances'
for file in os.listdir(folder):
    if file.endswith(('.xlsx', '.xlsb')):
        try:
            res = extract_financials(os.path.join(folder, file))
            res['file'] = file
            data.append(res)
        except Exception as e:
            print(f"Failed {file}: {e}")

import json
print(json.dumps(data, indent=2))
