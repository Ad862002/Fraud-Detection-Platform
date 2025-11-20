import pandas as pd

def apply_business_rules(df):
    """
    Applies simple business rules to flag potentially fraudulent transactions.
    Returns DataFrame with 'risk_reason' and 'rule_score' columns.
    """
    df = df.copy()
    df['risk_reason'] = ''
    df['rule_score'] = 0
    
    # Calculate customer behavior metrics
    customer_stats = df.groupby('customer_id').agg({
        'amount': ['mean', 'std'],
        'country': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'US'
    }).round(2)
    customer_stats.columns = ['avg_amount', 'std_amount', 'usual_country']
    customer_stats = customer_stats.reset_index()
    
    df = df.merge(customer_stats, on='customer_id', how='left')
    
    # Rule 1: Unusually high amount (> 3x average)
    high_amount_mask = df['amount'] > (3 * df['avg_amount'])
    df.loc[high_amount_mask, 'risk_reason'] += 'HIGH_AMOUNT;'
    df.loc[high_amount_mask, 'rule_score'] += 2
    
    # Rule 2: Unusual country
    unusual_country_mask = df['country'] != df['usual_country']
    df.loc[unusual_country_mask, 'risk_reason'] += 'UNUSUAL_COUNTRY;'
    df.loc[unusual_country_mask, 'rule_score'] += 1
    
    # Rule 3: Rapid transactions (within 10 minutes of previous)
    df['time_since_last'] = df.groupby('customer_id')['timestamp'].diff().dt.total_seconds() / 60
    rapid_mask = df['time_since_last'] < 10
    df.loc[rapid_mask, 'risk_reason'] += 'RAPID_SUCCESSION;'
    df.loc[rapid_mask, 'rule_score'] += 1
    
    # Clean up temporary columns
    df = df.drop(['avg_amount', 'std_amount', 'usual_country', 'time_since_last'], axis=1)
    
    return df

if __name__ == "__main__":
    # Test the rules
    from prepare_data import prepare_data
    df = prepare_data('data/raw/transactions.csv', 'data/processed/transactions.parquet')
    df_with_rules = apply_business_rules(df)
    print(f"Found {len(df_with_rules[df_with_rules['rule_score'] > 0])} potentially suspicious transactions")
