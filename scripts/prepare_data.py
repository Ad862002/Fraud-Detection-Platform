import pandas as pd
import numpy as np
from pathlib import Path

def prepare_data(input_path, output_path):
    """Normalizes raw transaction data into a clean, analysis-ready format."""
    
    # Read data
    df = pd.read_csv(input_path, parse_dates=['timestamp'])
    
    # 1. Fill missing merchants
    df['merchant'] = df['merchant'].fillna('UNKNOWN_MERCHANT')
    
    # 2. Standardize country codes (example: convert to uppercase)
    df['country'] = df['country'].str.upper()
    
    # 3. Add useful time-based features
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.day_name()
    df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])
    
    # 4. Sort by customer and timestamp for analysis
    df = df.sort_values(['customer_id', 'timestamp'])
    
    # Save processed data
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
    
    # Print schema summary
    print("\nSchema Summary:")
    print(df.dtypes)
    
    return df

if __name__ == "__main__":
    prepare_data(
        input_path='data/raw/transactions.csv',
        output_path='data/processed/transactions.parquet'
    )
