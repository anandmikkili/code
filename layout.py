"""
layout.py — Dash app layout (UI structure).

Components
----------
region-dropdown  : first dropdown; options are seeded by a callback on page load.
product-dropdown : second dropdown; options depend on the selected region.
sales-table      : placeholder div; filled with a DataTable by a callback.
init-store       : hidden dcc.Store whose data fires the initialisation callback.

All callback logic lives in callbacks.py.
"""

from dash import dcc, html


def create_layout(app) -> html.Div:
    """Return the top-level layout component for the Dash app."""
    return html.Div(
        style={
            "fontFamily": "Arial, sans-serif",
            "maxWidth": "900px",
            "margin": "0 auto",
            "padding": "32px 24px",
        },
        children=[

            # ── Header ────────────────────────────────────────────────────────
            html.H1(
                "Regional Sales Dashboard",
                style={"textAlign": "center", "color": "#2c3e50", "marginBottom": "4px"},
            ),
            html.P(
                "Select a region, then a product to view monthly sales data.",
                style={"textAlign": "center", "color": "#7f8c8d", "marginBottom": "32px"},
            ),

            # ── Dropdowns row ─────────────────────────────────────────────────
            html.Div(
                style={"display": "flex", "gap": "24px", "flexWrap": "wrap", "marginBottom": "32px"},
                children=[

                    # First dropdown — Region
                    # Options and default value are set by the populate_regions callback.
                    html.Div(
                        style={"flex": "1", "minWidth": "200px"},
                        children=[
                            html.Label(
                                "Region",
                                style={
                                    "fontWeight": "bold",
                                    "fontSize": "14px",
                                    "marginBottom": "6px",
                                    "display": "block",
                                    "color": "#34495e",
                                },
                            ),
                            dcc.Dropdown(
                                id="region-dropdown",
                                options=[],      # populated via callback
                                value=None,
                                placeholder="Select a region…",
                                clearable=False,
                            ),
                        ],
                    ),

                    # Second dropdown — Product
                    # Options are rebuilt by the populate_products callback each
                    # time the region changes, so different regions can expose
                    # different product sets.
                    html.Div(
                        style={"flex": "1", "minWidth": "200px"},
                        children=[
                            html.Label(
                                "Product",
                                style={
                                    "fontWeight": "bold",
                                    "fontSize": "14px",
                                    "marginBottom": "6px",
                                    "display": "block",
                                    "color": "#34495e",
                                },
                            ),
                            dcc.Dropdown(
                                id="product-dropdown",
                                options=[],      # populated via callback
                                value=None,
                                placeholder="Select a product…",
                                clearable=False,
                                disabled=True,   # enabled once a region is chosen
                            ),
                        ],
                    ),
                ],
            ),

            # ── Sales table ───────────────────────────────────────────────────
            html.Div(id="sales-table"),

            # ── Hidden store — triggers the region-dropdown callback on load ──
            dcc.Store(id="init-store", data=True),
        ],
    )
