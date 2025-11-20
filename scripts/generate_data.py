import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_transactions(n_customers=1000, n_transactions=50000):
    np.random.seed(42)
    
    # Generate customer profiles
    customers = [f"CUST_{i:05d}" for i in range(n_customers)]
    customer_countries = {cust: np.random.choice(['US', 'CA', 'UK', 'FR', 'DE']) for cust in customers}
    
    # Generate transactions
    data = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(n_transactions):
        cust_id = np.random.choice(customers)
        base_amount = np.random.lognormal(3, 1.5)  # Most transactions are small
        amount = round(min(base_amount, 5000), 2)  # Cap at 5000
        
        # Random timestamp within the year
        days_offset = np.random.randint(0, 365)
        hours_offset = np.random.randint(0, 24)
        timestamp = start_date + timedelta(days=days_offset, hours=hours_offset)
        
        # Merchant and channel
        merchant = np.random.choice(['AMAZON', 'STARBUCKS', 'WALMART', 'NETFLIX', 'SPOTIFY', 'GROCERY_STORE', 'GAS_STATION', None], p=[0.2, 0.15, 0.15, 0.1, 0.1, 0.15, 0.1, 0.05])
        channel = np.random.choice(['online', 'pos', 'atm', 'transfer'])
        
        # Usually the customer's country, but sometimes foreign
        country = customer_countries[cust_id]
        if np.random.random() < 0.05:  # 5% foreign transactions
            country = np.random.choice(['CN', 'RU', 'BR', 'NG', 'IN'])  # Suspicious countries
        
        data.append([cust_id, amount, timestamp, merchant, channel, country])
    
    df = pd.DataFrame(data, columns=['customer_id', 'amount', 'timestamp', 'merchant', 'channel', 'country'])
    
    # Introduce some missing values
    df.loc[df.sample(frac=0.03).index, 'merchant'] = None
    
    return df

if __name__ == "__main__":
    df = generate_transactions()
    df.to_csv('data/raw/transactions.csv', index=False)
    print(f"Generated {len(df)} transactions for demo. Saved to data/raw/transactions.csv")
