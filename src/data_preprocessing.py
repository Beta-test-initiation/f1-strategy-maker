import pandas as pd

def preprocess_data(file_path):
    print(f"Loading data from {file_path}")
    df = pd.read_csv(file_path)
    
    # Check actual column names
    print("Column names:", df.columns)
    
    # Drop rows with NaN values in any column
    df = df.dropna()
    
    # Reset index after dropping rows
    df = df.reset_index(drop=True)
    
    return df
