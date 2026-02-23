"""
data.py — Sample DataFrame used by the app.

The DataFrame contains quarterly sales figures broken down by region and
product line, used to demonstrate 2-dropdown filtering with a DataTable.

Columns:
    region     : sales region (North / South / East / West)
    product    : product line (Product A / B / C)
    quarter    : fiscal quarter (Q1–Q4)
    units_sold : units sold in that period
    revenue    : revenue in USD
    profit     : profit in USD
"""

import random
import itertools

import pandas as pd

random.seed(42)

REGIONS   = ["North", "South", "East", "West"]
PRODUCTS  = ["Product A", "Product B", "Product C"]
QUARTERS  = ["Q1", "Q2", "Q3", "Q4"]

rows = []
for region, product, quarter in itertools.product(REGIONS, PRODUCTS, QUARTERS):
    rows.append(
        {
            "region":     region,
            "product":    product,
            "quarter":    quarter,
            "units_sold": random.randint(100, 500),
            "revenue":    random.randint(10_000, 50_000),
            "profit":     random.randint(2_000, 15_000),
        }
    )

df = pd.DataFrame(rows)

REGION_OPTIONS  = [{"label": r, "value": r} for r in REGIONS]
PRODUCT_OPTIONS = [{"label": p, "value": p} for p in PRODUCTS]
