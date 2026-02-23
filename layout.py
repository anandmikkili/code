"""
layout.py — Dash app layout (UI structure only).

All visual components are defined here and returned via create_layout().
No business logic or data fetching lives in this file.

Callback-driven components start with empty options / data; the callbacks
in callbacks.py populate them at runtime.

Components
----------
dcc.Location      : triggers the initial page-load callback for Dropdown 1
category-dropdown : Dropdown 1 — top-level category (options from callback)
subcategory-dropdown : Dropdown 2 — sub-category (options cascade from DD1)
products-table    : DataTable — rows populated when both dropdowns have values
status-text       : plain-text breadcrumb / hint updated by the table callback
"""

from dash import dcc, html, dash_table


# ── Static table column definitions ───────────────────────────────────────────

TABLE_COLUMNS = [
    {"name": "Product",   "id": "Product"},
    {"name": "Brand",     "id": "Brand"},
    {"name": "Price ($)", "id": "Price ($)", "type": "numeric"},
    {"name": "Stock",     "id": "Stock",     "type": "numeric"},
    {"name": "Rating",    "id": "Rating",    "type": "numeric"},
]

# ── Shared styles ──────────────────────────────────────────────────────────────

_LABEL_STYLE = {"fontWeight": "bold", "marginBottom": "6px", "display": "block", "color": "#333"}
_CARD_STYLE  = {
    "backgroundColor": "white",
    "borderRadius": "8px",
    "boxShadow": "0 2px 8px rgba(0,0,0,0.08)",
    "padding": "20px",
}


# ── Layout factory ─────────────────────────────────────────────────────────────

def create_layout() -> html.Div:
    """Return the top-level layout component for the Dash app."""

    return html.Div(
        style={
            "fontFamily": "Arial, sans-serif",
            "maxWidth": "1040px",
            "margin": "0 auto",
            "padding": "32px 24px",
            "backgroundColor": "#f4f6f9",
            "minHeight": "100vh",
        },
        children=[

            # ── Hidden location — fires on page load to populate DD1 ───────────
            dcc.Location(id="_url", refresh=False),

            # ── Page header ────────────────────────────────────────────────────
            html.H1(
                "Product Catalogue Explorer",
                style={"textAlign": "center", "color": "#1a1a2e", "marginBottom": "4px"},
            ),
            html.P(
                "Use the dropdowns below to filter products by category and sub-category.",
                style={"textAlign": "center", "color": "#666", "marginBottom": "28px"},
            ),

            # ── Dropdown card ──────────────────────────────────────────────────
            html.Div(
                style={**_CARD_STYLE, "marginBottom": "20px"},
                children=[
                    html.Div(
                        style={"display": "flex", "gap": "24px", "flexWrap": "wrap"},
                        children=[

                            # ── Dropdown 1 : Category ──────────────────────────
                            html.Div(
                                style={"flex": "1", "minWidth": "220px"},
                                children=[
                                    html.Label("Category", style=_LABEL_STYLE),
                                    dcc.Dropdown(
                                        id="category-dropdown",
                                        options=[],          # filled by populate_category_dropdown()
                                        value=None,
                                        placeholder="Select a category…",
                                        clearable=True,
                                    ),
                                ],
                            ),

                            # ── Dropdown 2 : Sub-category (linked to DD1) ──────
                            html.Div(
                                style={"flex": "1", "minWidth": "220px"},
                                children=[
                                    html.Label("Sub-Category", style=_LABEL_STYLE),
                                    dcc.Dropdown(
                                        id="subcategory-dropdown",
                                        options=[],          # filled by update_subcategory_dropdown()
                                        value=None,
                                        placeholder="Select a sub-category…",
                                        disabled=True,       # enabled when DD1 has a value
                                        clearable=True,
                                    ),
                                ],
                            ),

                        ],
                    ),
                ],
            ),

            # ── Status / breadcrumb text ───────────────────────────────────────
            html.Div(
                id="status-text",
                style={
                    "color": "#888",
                    "marginBottom": "12px",
                    "fontStyle": "italic",
                    "minHeight": "20px",
                },
            ),

            # ── Data Table card ────────────────────────────────────────────────
            html.Div(
                style={**_CARD_STYLE, "padding": "0", "overflow": "hidden"},
                children=[
                    dash_table.DataTable(
                        id="products-table",
                        columns=TABLE_COLUMNS,
                        data=[],                    # filled by update_table()
                        sort_action="native",        # client-side column sorting
                        filter_action="native",      # client-side per-column filtering
                        page_action="native",
                        page_size=10,
                        style_table={"overflowX": "auto"},
                        style_header={
                            "backgroundColor": "#1a1a2e",
                            "color": "white",
                            "fontWeight": "bold",
                            "textAlign": "center",
                            "padding": "12px 16px",
                            "border": "none",
                        },
                        style_cell={
                            "textAlign": "left",
                            "padding": "10px 16px",
                            "fontFamily": "Arial, sans-serif",
                            "fontSize": "14px",
                            "border": "none",
                            "borderBottom": "1px solid #f0f0f0",
                        },
                        style_cell_conditional=[
                            # Centre numeric columns
                            {"if": {"column_id": col}, "textAlign": "center"}
                            for col in ("Price ($)", "Stock", "Rating")
                        ],
                        style_data_conditional=[
                            # Zebra striping
                            {
                                "if": {"row_index": "odd"},
                                "backgroundColor": "#fafafa",
                            },
                            # Highlight high-rated products
                            {
                                "if": {"filter_query": "{Rating} >= 4.7"},
                                "backgroundColor": "#eafaf1",
                                "color": "#1e8449",
                                "fontWeight": "bold",
                            },
                        ],
                    ),
                ],
            ),

        ],
    )
