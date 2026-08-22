import pandas as pd
import os

def extract_financials(filepath):
    # Load with header=None so we can see all rows and columns
    df = pd.read_excel(filepath, header=None)
    
    data = {
        'checking': None,
        'money_market': None,
        'total_funds': None
    }
    
    # Iterate through all cells, find keywords, and pick the number immediately to the right or in the same row
    for i, row in df.iterrows():
        for j, cell in enumerate(row):
            cell_str = str(cell)
            
            # Look for keywords
            if 'Checking' in cell_str:
                # Look for number in the same row
                for next_col in range(j + 1, len(row)):
                    if isinstance(row[next_col], (int, float)):
                        data['checking'] = row[next_col]
                        break
            
            elif 'Money Market' in cell_str or 'CD' in cell_str:
                for next_col in range(j + 1, len(row)):
                    if isinstance(row[next_col], (int, float)):
                        data['money_market'] = row[next_col]
                        break
                        
            elif 'Total' in cell_str and 'Funds' in cell_str:
                for next_col in range(j + 1, len(row)):
                    if isinstance(row[next_col], (int, float)):
                        data['total_funds'] = row[next_col]
                        break
    return data

# Test again
print(extract_financials('src/data/finances/SCCA_073120.xlsx'))
