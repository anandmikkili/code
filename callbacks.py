"""
callbacks.py — Dash callback definitions.

Importing this module registers all callbacks with the global Dash app
instance, so app.py only needs `import callbacks`.

Callbacks
---------
update_table_and_stats
    Inputs  : region-dropdown, product-dropdown
    Outputs : sales-table (DataTable), summary-stats (KPI cards)
"""

from dash import Input, Output, callback, dash_table, html

from data import df


# ── Helper: KPI stat card ──────────────────────────────────────────────────────

def _stat_card(label: str, value: str) -> html.Div:
    """Return a styled card displaying a single KPI metric."""
    return html.Div(
        style={
            "background":    "#f0f4f8",
            "border":        "1px solid #d0d8e4",
            "borderRadius":  "8px",
            "padding":       "12px 20px",
            "textAlign":     "center",
            "minWidth":      "140px",
        },
        children=[
            html.Div(
                label,
                style={
                    "fontSize":      "11px",
                    "color":         "#666",
                    "textTransform": "uppercase",
                    "letterSpacing": "0.05em",
                    "marginBottom":  "4px",
                },
            ),
            html.Div(
                value,
                style={
                    "fontSize":   "22px",
                    "fontWeight": "bold",
                    "color":      "#333",
                },
            ),
        ],
    )


# ── Callback: filter table + update KPI cards ──────────────────────────────────

@callback(
    Output("sales-table",   "children"),
    Output("summary-stats", "children"),
    Input("region-dropdown",  "value"),
    Input("product-dropdown", "value"),
)
def update_table_and_stats(selected_region: str | None, selected_product: str | None):
    """
    Filter the DataFrame by the two dropdowns and render:
      - A DataTable showing matching rows
      - A row of KPI summary cards

    Parameters
    ----------
    selected_region  : value from region-dropdown, or None (show all)
    selected_product : value from product-dropdown, or None (show all)

    Returns
    -------
    (dash_table.DataTable, html.Div)
    """
    filtered = df.copy()

    if selected_region:
        filtered = filtered[filtered["region"] == selected_region]
    if selected_product:
        filtered = filtered[filtered["product"] == selected_product]

    # ── KPI summary cards ──────────────────────────────────────────────────────
    summary = html.Div(
        style={"display": "flex", "gap": "12px", "flexWrap": "wrap"},
        children=[
            _stat_card("Rows",          f"{len(filtered):,}"),
            _stat_card("Total Units",   f"{filtered['units_sold'].sum():,}"),
            _stat_card("Total Revenue", f"${filtered['revenue'].sum():,}"),
            _stat_card("Total Profit",  f"${filtered['profit'].sum():,}"),
        ],
    )

    # ── DataTable ──────────────────────────────────────────────────────────────
    table = dash_table.DataTable(
        data=filtered.to_dict("records"),
        columns=[
            {"name": "Region",      "id": "region"},
            {"name": "Product",     "id": "product"},
            {"name": "Quarter",     "id": "quarter"},
            {"name": "Units Sold",  "id": "units_sold"},
            {"name": "Revenue ($)", "id": "revenue"},
            {"name": "Profit ($)",  "id": "profit"},
        ],
        # Built-in sort and filter controls
        sort_action="native",
        filter_action="native",
        # Pagination
        page_size=10,
        page_action="native",
        # Styling
        style_table={"overflowX": "auto"},
        style_header={
            "backgroundColor": "#1f77b4",
            "color":           "white",
            "fontWeight":      "bold",
            "textAlign":       "center",
        },
        style_cell={
            "textAlign":  "center",
            "padding":    "8px 12px",
            "fontFamily": "Arial, sans-serif",
            "fontSize":   "14px",
        },
        style_data_conditional=[
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "#f9f9f9",
            },
        ],
    )

    return table, summary
