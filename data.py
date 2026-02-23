"""
data.py — Nested product catalogue data and helper functions.

Structure
---------
CATALOGUE[category][sub_category] = list[dict]

Each record has the keys:
    Product, Brand, Price ($), Stock, Rating
"""

# ---------------------------------------------------------------------------
# Raw data
# ---------------------------------------------------------------------------

CATALOGUE: dict[str, dict[str, list[dict]]] = {
    "Electronics": {
        "Smartphones": [
            {"Product": "iPhone 15 Pro",  "Brand": "Apple",   "Price ($)": 999,  "Stock": 120, "Rating": 4.8},
            {"Product": "Galaxy S24",     "Brand": "Samsung", "Price ($)": 899,  "Stock":  85, "Rating": 4.7},
            {"Product": "Pixel 8",        "Brand": "Google",  "Price ($)": 699,  "Stock":  60, "Rating": 4.5},
            {"Product": "OnePlus 12",     "Brand": "OnePlus", "Price ($)": 649,  "Stock":  45, "Rating": 4.4},
        ],
        "Laptops": [
            {"Product": "MacBook Pro 14", "Brand": "Apple",     "Price ($)": 1999, "Stock": 40, "Rating": 4.9},
            {"Product": "ThinkPad X1",   "Brand": "Lenovo",    "Price ($)": 1499, "Stock": 55, "Rating": 4.6},
            {"Product": "XPS 15",        "Brand": "Dell",      "Price ($)": 1799, "Stock": 30, "Rating": 4.7},
            {"Product": "Surface Pro 9", "Brand": "Microsoft", "Price ($)": 1299, "Stock": 50, "Rating": 4.5},
        ],
        "Headphones": [
            {"Product": "WH-1000XM5",     "Brand": "Sony",  "Price ($)": 349, "Stock": 100, "Rating": 4.8},
            {"Product": "AirPods Pro",    "Brand": "Apple", "Price ($)": 249, "Stock": 200, "Rating": 4.7},
            {"Product": "QuietComfort 45","Brand": "Bose",  "Price ($)": 329, "Stock":  75, "Rating": 4.6},
        ],
    },
    "Clothing": {
        "Men's Wear": [
            {"Product": "Oxford Shirt",       "Brand": "Brooks Brothers", "Price ($)":  89, "Stock": 150, "Rating": 4.3},
            {"Product": "Slim Fit Chinos",    "Brand": "Gap",             "Price ($)":  59, "Stock": 200, "Rating": 4.2},
            {"Product": "Merino Sweater",     "Brand": "Uniqlo",          "Price ($)":  79, "Stock": 120, "Rating": 4.5},
            {"Product": "Denim Jacket",       "Brand": "Levi's",          "Price ($)":  99, "Stock":  80, "Rating": 4.4},
        ],
        "Women's Wear": [
            {"Product": "Floral Wrap Dress",  "Brand": "Zara",    "Price ($)":  69, "Stock":  90, "Rating": 4.3},
            {"Product": "High-Waist Jeans",   "Brand": "Levi's",  "Price ($)":  89, "Stock": 110, "Rating": 4.4},
            {"Product": "Cashmere Cardigan",  "Brand": "Everlane","Price ($)": 129, "Stock":  60, "Rating": 4.6},
        ],
        "Footwear": [
            {"Product": "Air Max 270",    "Brand": "Nike",   "Price ($)": 150, "Stock": 130, "Rating": 4.6},
            {"Product": "Stan Smith",     "Brand": "Adidas", "Price ($)":  90, "Stock": 180, "Rating": 4.5},
            {"Product": "Ultraboost 22",  "Brand": "Adidas", "Price ($)": 190, "Stock":  70, "Rating": 4.7},
            {"Product": "Classic Leather","Brand": "Reebok", "Price ($)":  75, "Stock":  95, "Rating": 4.3},
        ],
    },
    "Furniture": {
        "Living Room": [
            {"Product": "3-Seat Sofa",   "Brand": "IKEA",     "Price ($)": 599, "Stock": 25, "Rating": 4.2},
            {"Product": "Coffee Table",  "Brand": "West Elm", "Price ($)": 349, "Stock": 40, "Rating": 4.4},
            {"Product": "Bookshelf",     "Brand": "IKEA",     "Price ($)": 199, "Stock": 60, "Rating": 4.3},
            {"Product": "Floor Lamp",    "Brand": "CB2",      "Price ($)": 149, "Stock": 55, "Rating": 4.5},
        ],
        "Bedroom": [
            {"Product": "King Bed Frame","Brand": "Ashley",       "Price ($)": 799, "Stock": 15, "Rating": 4.4},
            {"Product": "Nightstand",    "Brand": "IKEA",         "Price ($)":  89, "Stock": 80, "Rating": 4.2},
            {"Product": "Dresser",       "Brand": "Pottery Barn", "Price ($)": 699, "Stock": 20, "Rating": 4.5},
        ],
        "Office": [
            {"Product": "Standing Desk",    "Brand": "Uplift",       "Price ($)":  699, "Stock": 30, "Rating": 4.7},
            {"Product": "Ergonomic Chair",  "Brand": "Herman Miller","Price ($)": 1495, "Stock": 12, "Rating": 4.9},
            {"Product": "Monitor Stand",    "Brand": "Flexispot",    "Price ($)":   79, "Stock": 100,"Rating": 4.4},
        ],
    },
    "Food & Beverage": {
        "Coffee": [
            {"Product": "Ethiopia Yirgacheffe","Brand": "Blue Bottle","Price ($)": 22, "Stock": 300, "Rating": 4.8},
            {"Product": "House Blend",         "Brand": "Starbucks", "Price ($)": 14, "Stock": 500, "Rating": 4.3},
            {"Product": "Dark Roast",          "Brand": "Peet's",    "Price ($)": 16, "Stock": 400, "Rating": 4.5},
            {"Product": "Decaf Espresso",      "Brand": "Illy",      "Price ($)": 18, "Stock": 200, "Rating": 4.4},
        ],
        "Snacks": [
            {"Product": "Mixed Nuts",       "Brand": "Planters",     "Price ($)":  9, "Stock": 600, "Rating": 4.4},
            {"Product": "Dark Chocolate",   "Brand": "Lindt",        "Price ($)":  5, "Stock": 800, "Rating": 4.7},
            {"Product": "Kettle Chips",     "Brand": "Kettle Brand", "Price ($)":  4, "Stock": 700, "Rating": 4.5},
        ],
        "Beverages": [
            {"Product": "Sparkling Water 12-Pack","Brand": "LaCroix",       "Price ($)":  7, "Stock": 400, "Rating": 4.4},
            {"Product": "Green Tea",              "Brand": "Harney & Sons", "Price ($)": 12, "Stock": 350, "Rating": 4.6},
            {"Product": "Orange Juice",           "Brand": "Tropicana",     "Price ($)":  6, "Stock": 450, "Rating": 4.3},
        ],
    },
}

# ---------------------------------------------------------------------------
# Helper functions used by callbacks
# ---------------------------------------------------------------------------

def get_categories() -> list[dict]:
    """Return Dropdown options for all top-level categories."""
    return [{"label": cat, "value": cat} for cat in CATALOGUE]


def get_subcategories(category: str | None) -> list[dict]:
    """Return Dropdown options for sub-categories of the given category."""
    if category and category in CATALOGUE:
        return [{"label": sub, "value": sub} for sub in CATALOGUE[category]]
    return []


def get_products(category: str | None, subcategory: str | None) -> list[dict]:
    """Return product records for the given category + sub-category pair."""
    if (
        category
        and subcategory
        and category in CATALOGUE
        and subcategory in CATALOGUE[category]
    ):
        return CATALOGUE[category][subcategory]
    return []
