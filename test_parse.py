import pandas as pd
import os

def parse_finance_file(filepath):
    # Try reading with header=None to see all rows
    df = pd.read_excel(filepath, header=None)
    
    # We need to find key metrics
    # Checking, Money Market, Total Funds, YTD Expenses
    # Let's extract values based on string matching in column 0
    
    data = {}
    
    # Simple extraction logic
    for i, row in df.iterrows():
        val = str(row[0])
        if 'Checking as of' in val:
            data['checking'] = row[1]
        elif 'Money Market/CD' in val:
            data['money_market'] = row[1]
        elif 'Total Funds' in val:
            data['total_funds'] = row[1]
            
    return data

# Test on a few
print(parse_finance_file('src/data/finances/SCCA_073120.xlsx'))
