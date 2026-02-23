"""
callbacks.py — Callback definitions for the Regional Sales Dashboard.

Importing this module registers all callbacks with the global Dash app instance
(via @callback), so app.py only needs `import callbacks`.

Callbacks
---------
1. populate_regions   — fires on page load; seeds the region dropdown.
2. populate_products  — fires when the region changes; rebuilds the product dropdown.
3. update_table       — fires when region or product changes; renders the DataTable.
"""

import dash
from dash import Input, Output, callback, dash_table

from data import MONTHS, SALES_DATA


# ── 1. Populate region dropdown on page load ───────────────────────────────────

@callback(
    Output("region-dropdown", "options"),
    Output("region-dropdown", "value"),
    Input("init-store", "data"),
)
def populate_regions(_trigger) -> tuple[list[dict], str]:
    """
    Seed the region dropdown with every region in SALES_DATA.
    Runs once on page load because init-store is a dcc.Store with data=True.
    The first region (alphabetically) is selected by default.
    """
    regions = sorted(SALES_DATA.keys())
    options = [{"label": r, "value": r} for r in regions]
    return options, regions[0]


# ── 2. Populate product dropdown when region changes ───────────────────────────

@callback(
    Output("product-dropdown", "options"),
    Output("product-dropdown", "value"),
    Output("product-dropdown", "disabled"),
    Input("region-dropdown", "value"),
)
def populate_products(region: str | None) -> tuple[list[dict], str | None, bool]:
    """
    Rebuild the product dropdown whenever the selected region changes.

    Different regions carry different product sets, so the options list
    is re-derived from SALES_DATA each time.
    The first product (alphabetically) within the new region is auto-selected.
    The dropdown is disabled when no region is chosen.
    """
    if not region:
        return [], None, True

    products = sorted(SALES_DATA[region].keys())
    options = [{"label": p, "value": p} for p in products]
    return options, products[0], False


# ── 3. Render sales table when region or product changes ───────────────────────

@callback(
    Output("sales-table", "children"),
    Input("region-dropdown", "value"),
    Input("product-dropdown", "value"),
)
def update_table(region: str | None, product: str | None):
    """
    Build and return a DataTable showing month-by-month sales for the
    selected region + product combination.

    Columns
    -------
    Month        : calendar month label
    Units Sold   : units sold that month
    MoM Change   : difference vs. the previous month (blank for January)

    A summary row is appended showing the annual total and monthly average.
    """
    if not region or not product:
        return dash.no_update

    monthly = SALES_DATA.get(region, {}).get(product)
    if not monthly:
        return dash.no_update

    # Build per-month rows
    records = []
    for i, (month, units) in enumerate(zip(MONTHS, monthly)):
        change = units - monthly[i - 1] if i > 0 else None
        if change is None:
            change_str = "—"
        elif change > 0:
            change_str = f"+{change}"
        else:
            change_str = str(change)

        records.append({
            "Month":      month,
            "Units Sold": units,
            "MoM Change": change_str,
        })

    # Summary row
    total = sum(monthly)
    avg   = total / len(monthly)
    records.append({
        "Month":      "Total / Avg",
        "Units Sold": total,
        "MoM Change": f"avg {avg:.1f}",
    })

    return dash_table.DataTable(
        id="sales-data-table",
        data=records,
        columns=[{"name": c, "id": c} for c in ["Month", "Units Sold", "MoM Change"]],
        style_table={"overflowX": "auto", "borderRadius": "6px", "overflow": "hidden"},
        style_header={
            "backgroundColor": "#2c3e50",
            "color": "white",
            "fontWeight": "bold",
            "textAlign": "center",
            "padding": "10px 14px",
            "fontSize": "14px",
        },
        style_cell={
            "textAlign": "center",
            "padding": "9px 14px",
            "fontFamily": "Arial, sans-serif",
            "fontSize": "14px",
            "border": "1px solid #e0e0e0",
        },
        style_data_conditional=[
            # Alternate row shading
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "#f4f6f7",
            },
            # Highlight the summary row
            {
                "if": {"filter_query": '{Month} = "Total / Avg"'},
                "fontWeight": "bold",
                "backgroundColor": "#d5e8d4",
                "color": "#1e8449",
            },
            # Green for positive MoM change
            {
                "if": {
                    "filter_query": '{MoM Change} contains "+"',
                    "column_id": "MoM Change",
                },
                "color": "#1e8449",
                "fontWeight": "bold",
            },
            # Red for negative MoM change
            {
                "if": {
                    "filter_query": '{MoM Change} contains "-"',
                    "column_id": "MoM Change",
                },
                "color": "#c0392b",
                "fontWeight": "bold",
            },
        ],
        page_action="none",
    )
