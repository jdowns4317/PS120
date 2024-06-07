import pandas as pd

def csv_to_tab(csv_filepath, tab_filepath):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_filepath)
    
    # Write the DataFrame to a .tab file using tab as a separator
    df.to_csv(tab_filepath, sep='\t', index=False)

# Usage
csv_filepath = 'data/CES20_Common_OUTPUT_vv.csv'  # The path to your CSV file
tab_filepath = 'data/CESdata2020.tab'  # The desired path for the .tab file

csv_to_tab(csv_filepath, tab_filepath)
