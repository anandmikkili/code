"""
data.py — Hierarchical sales data used by the app.

Data is organized as:
    SALES_DATA[region][product] = [12 monthly unit sales values]

MONTHS provides the 12 month labels aligned with those lists.
"""

MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]

# Each region carries a different product mix to demonstrate
# that the product dropdown options genuinely depend on the region.
SALES_DATA = {
    "North": {
        "Laptops":  [150, 160, 170, 180, 190, 200, 195, 210, 220, 230, 240, 250],
        "Phones":   [200, 210, 205, 220, 230, 245, 240, 255, 260, 270, 280, 295],
        "Tablets":  [ 80,  85,  90,  88,  95, 100,  98, 105, 110, 115, 120, 130],
    },
    "South": {
        "Laptops":  [110, 120, 130, 125, 135, 145, 140, 150, 160, 170, 175, 185],
        "Monitors": [ 60,  65,  70,  75,  80,  85,  82,  90,  95, 100, 105, 115],
        "Keyboards":[ 40,  45,  50,  48,  55,  60,  58,  65,  70,  72,  78,  85],
    },
    "East": {
        "Phones":   [180, 190, 185, 200, 210, 220, 215, 225, 235, 245, 255, 265],
        "Tablets":  [ 70,  75,  80,  85,  90,  95,  92, 100, 105, 110, 118, 125],
        "Printers": [ 30,  35,  32,  38,  42,  45,  44,  50,  55,  58,  62,  68],
    },
    "West": {
        "Laptops":  [130, 140, 145, 150, 160, 170, 165, 175, 185, 195, 205, 215],
        "Monitors": [ 55,  60,  65,  70,  75,  80,  78,  85,  90,  95, 100, 110],
        "Phones":   [160, 170, 165, 175, 185, 195, 190, 200, 210, 220, 228, 238],
    },
}
