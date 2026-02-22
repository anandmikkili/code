"""
callbacks.py — Dash callback definitions.

Importing this module registers all callbacks with the global `dash.get_app()`
instance, so app.py only needs `import callbacks`.
"""

import dash
from dash import Input, Output, callback, dash_table
import plotly.graph_objects as go

from data import df, PRODUCT_OPTIONS, MARKER_SYMBOLS, LINE_COLORS


# ── Helper: build figure ───────────────────────────────────────────────────────

def _build_figure(
    selected_products: list[str],
    marker_size: int | float,
    line_width: int | float,
) -> go.Figure:
    """
    Construct a Plotly Figure containing one line+marker trace per product.

    Parameters
    ----------
    selected_products : list of column names from the DataFrame
    marker_size       : size of the marker symbol
    line_width        : width of the connecting line

    Returns
    -------
    go.Figure
    """
    fig = go.Figure()

    for idx, product in enumerate(selected_products):
        label  = next(o["label"] for o in PRODUCT_OPTIONS if o["value"] == product)
        color  = LINE_COLORS[idx % len(LINE_COLORS)]
        symbol = MARKER_SYMBOLS[idx % len(MARKER_SYMBOLS)]

        fig.add_trace(
            go.Scatter(
                x=df["month"],
                y=df[product],
                mode="lines+markers",          # line with markers
                name=label,
                line=dict(
                    color=color,
                    width=line_width,
                ),
                marker=dict(
                    symbol=symbol,
                    size=marker_size,
                    color=color,
                    line=dict(color="white", width=1.5),  # white border for visibility
                ),
                hovertemplate=(
                    "<b>%{fullData.name}</b><br>"
                    "Month : %{x}<br>"
                    "Units  : %{y:,}<extra></extra>"
                ),
            )
        )

    # ── Separate layout definition ─────────────────────────────────────────────
    layout = go.Layout(
        title=dict(
            text="Monthly Sales by Product Line",
            x=0.5,
            xanchor="center",
            font=dict(size=18),
        ),
        xaxis=dict(
            title="Month",
            showgrid=True,
            gridcolor="#e0e0e0",
            zeroline=False,
        ),
        yaxis=dict(
            title="Units Sold",
            showgrid=True,
            gridcolor="#e0e0e0",
            zeroline=False,
            rangemode="tozero",
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        hovermode="x unified",
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(l=60, r=30, t=80, b=60),
    )

    fig.update_layout(layout)
    return fig


# ── Callback: update graph ─────────────────────────────────────────────────────

@callback(
    Output("line-graph", "figure"),
    Input("product-checklist",  "value"),
    Input("marker-size-slider", "value"),
    Input("line-width-slider",  "value"),
)
def update_graph(
    selected_products: list[str],
    marker_size: int | float,
    line_width: int | float,
) -> go.Figure:
    """Rebuild the line graph whenever the user changes any control."""
    if not selected_products:
        # Return an empty figure with a friendly message
        fig = go.Figure()
        fig.update_layout(
            title="Select at least one product to display",
            plot_bgcolor="white",
            paper_bgcolor="white",
        )
        return fig

    return _build_figure(selected_products, marker_size, line_width)


# ── Callback: update summary table ────────────────────────────────────────────

@callback(
    Output("summary-table", "children"),
    Input("product-checklist", "value"),
)
def update_summary_table(selected_products: list[str]):
    """Render a summary statistics table below the graph."""
    if not selected_products:
        return dash.no_update

    cols = ["month"] + selected_products
    visible_df = df[cols].copy()

    # Rename columns to human-friendly labels
    rename_map = {o["value"]: o["label"] for o in PRODUCT_OPTIONS}
    rename_map["month"] = "Month"
    visible_df = visible_df.rename(columns=rename_map)

    return dash_table.DataTable(
        data=visible_df.to_dict("records"),
        columns=[{"name": c, "id": c} for c in visible_df.columns],
        style_table={"overflowX": "auto"},
        style_header={
            "backgroundColor": "#1f77b4",
            "color": "white",
            "fontWeight": "bold",
            "textAlign": "center",
        },
        style_cell={
            "textAlign": "center",
            "padding": "8px",
            "fontFamily": "Arial, sans-serif",
        },
        style_data_conditional=[
            {"if": {"row_index": "odd"}, "backgroundColor": "#f9f9f9"},
        ],
        page_action="none",
    )
