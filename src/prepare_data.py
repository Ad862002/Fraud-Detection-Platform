#!/usr/bin/env python3
"""
Entry point for data preparation pipeline.
Usage: python src/prepare_data.py
"""
from scripts.prepare_data import prepare_data

if __name__ == "__main__":
    print("Starting data preparation...")
    prepare_data(
        input_path='data/raw/transactions.csv',
        output_path='data/processed/transactions.parquet'
    )
    print("Data preparation complete!")