# Fraud Detection Platform

A mini platform for detecting suspicious financial transactions, mimicking real-world AML (Anti-Money Laundering) systems.

## Data Flow
Raw Data → Cleaning → Rule Engine → ML Scoring → Risk Aggregation → Investigator UI

## Quick Start
1. `python scripts/generate_data.py`
2. `python prepare_data.py` 
3. `python rules.py`
4. `streamlit run app.py` (after building the UI)
