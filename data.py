"""
data.py — Sample DataFrame used by the app.

The DataFrame contains monthly sales figures for three product lines.
Columns:
    month      : calendar month label
    product_a  : units sold for Product A
    product_b  : units sold for Product B
    product_c  : units sold for Product C
"""

import pandas as pd

MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]

RAW_DATA = {
    "month": MONTHS,
    "product_a": [120, 135, 148, 162, 175, 190, 185, 200, 215, 230, 245, 260],
    "product_b": [80,  95, 105, 98,  112, 125, 118, 130, 142, 155, 160, 170],
    "product_c": [60,  70,  65,  80,  85,  90, 100,  95, 110, 118, 125, 140],
}

df = pd.DataFrame(RAW_DATA)

PRODUCT_OPTIONS = [
    {"label": "Product A", "value": "product_a"},
    {"label": "Product B", "value": "product_b"},
    {"label": "Product C", "value": "product_c"},
]

MARKER_SYMBOLS = ["circle", "square", "diamond"]
LINE_COLORS    = ["#1f77b4", "#ff7f0e", "#2ca02c"]
