"""
layout.py — Dash app layout (UI structure).

All visual components are defined here and returned via `create_layout()`.
The callback logic lives in callbacks.py.

Components
----------
- Dropdown 1 : filter by Region   (id="region-dropdown")
- Dropdown 2 : filter by Product  (id="product-dropdown")
- Summary bar : live KPI cards    (id="summary-stats")
- DataTable   : filtered records  (id="sales-table")
"""

from dash import dcc, html

from data import REGION_OPTIONS, PRODUCT_OPTIONS


def create_layout(app) -> html.Div:
    """Return the top-level layout component for the Dash app."""

    return html.Div(
        style={
            "fontFamily": "Arial, sans-serif",
            "maxWidth": "1000px",
            "margin": "0 auto",
            "padding": "24px",
        },
        children=[

            # ── Header ────────────────────────────────────────────────────────
            html.H1(
                "Sales Dashboard",
                style={"textAlign": "center", "color": "#333"},
            ),
            html.P(
                "Use the dropdowns to filter the table by region and product.",
                style={"textAlign": "center", "color": "#666", "marginBottom": "28px"},
            ),

            # ── Dropdowns row ─────────────────────────────────────────────────
            html.Div(
                style={
                    "display": "flex",
                    "gap": "24px",
                    "flexWrap": "wrap",
                    "marginBottom": "24px",
                },
                children=[

                    # Dropdown 1 — Region
                    html.Div(
                        style={"flex": "1", "minWidth": "200px"},
                        children=[
                            html.Label(
                                "Region",
                                style={
                                    "fontWeight": "bold",
                                    "marginBottom": "6px",
                                    "display": "block",
                                },
                            ),
                            dcc.Dropdown(
                                id="region-dropdown",
                                options=REGION_OPTIONS,
                                value=None,
                                placeholder="All Regions",
                                clearable=True,
                            ),
                        ],
                    ),

                    # Dropdown 2 — Product
                    html.Div(
                        style={"flex": "1", "minWidth": "200px"},
                        children=[
                            html.Label(
                                "Product",
                                style={
                                    "fontWeight": "bold",
                                    "marginBottom": "6px",
                                    "display": "block",
                                },
                            ),
                            dcc.Dropdown(
                                id="product-dropdown",
                                options=PRODUCT_OPTIONS,
                                value=None,
                                placeholder="All Products",
                                clearable=True,
                            ),
                        ],
                    ),
                ],
            ),

            # ── Summary KPI cards (populated by callback) ─────────────────────
            html.Div(id="summary-stats", style={"marginBottom": "20px"}),

            # ── DataTable (populated by callback) ─────────────────────────────
            html.Div(id="sales-table"),
        ],
    )
