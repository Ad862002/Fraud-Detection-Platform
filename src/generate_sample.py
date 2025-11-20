#!/usr/bin/env python3
"""
Entry point for generating sample transaction data.
Usage: python src/generate_sample.py
"""
from scripts.generate_data import generate_transactions

if __name__ == "__main__":
    print("Generating sample transaction data...")
    generate_transactions()
    print("Data generation complete! Check data/raw/transactions.csv")