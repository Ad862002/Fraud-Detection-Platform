#!/usr/bin/env python3
"""
Entry point for applying business rules.
Usage: python src/apply_rules.py
"""
from scripts.prepare_data import prepare_data
from scripts.rules import apply_business_rules

if __name__ == "__main__":
    print("Loading and preparing data...")
    df = prepare_data(
        input_path='data/raw/transactions.csv',
        output_path='data/processed/transactions.parquet'
    )
    
    print("Applying business rules...")
    df_with_rules = apply_business_rules(df)
    
    # Save results
    df_with_rules.to_parquet('data/processed/transactions_with_rules.parquet', index=False)
    
    suspicious_count = len(df_with_rules[df_with_rules['rule_score'] > 0])
    print(f"Rules applied! Found {suspicious_count} potentially suspicious transactions")