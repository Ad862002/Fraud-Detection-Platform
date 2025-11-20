"""
Fraud Detection Platform - Core Logic Modules
"""

from .generate_data import generate_transactions
from .prepare_data import prepare_data
from .rules import apply_business_rules

__all__ = [
    'generate_transactions',
    'prepare_data', 
    'apply_business_rules',
]

__version__ = "1.0.0"
