"""
layout.py — Dash app layout (UI structure).

All visual components are defined here and returned via `create_layout()`.
The callback logic lives in callbacks.py.
"""

from dash import dcc, html
from data import PRODUCT_OPTIONS


def create_layout(app) -> html.Div:
    """Return the top-level layout component for the Dash app."""

    return html.Div(
        style={"fontFamily": "Arial, sans-serif", "maxWidth": "960px", "margin": "0 auto", "padding": "24px"},
        children=[
            # ── Header ────────────────────────────────────────────────────────
            html.H1(
                "Monthly Sales — Line Graph with Markers",
                style={"textAlign": "center", "color": "#333"},
            ),
            html.P(
                "Select one or more product lines to display on the chart.",
                style={"textAlign": "center", "color": "#666"},
            ),

            # ── Controls ──────────────────────────────────────────────────────
            html.Div(
                style={"display": "flex", "gap": "24px", "flexWrap": "wrap", "marginBottom": "16px"},
                children=[
                    # Product selector (multi-select checklist)
                    html.Div(
                        style={"flex": "1", "minWidth": "200px"},
                        children=[
                            html.Label("Product Lines", style={"fontWeight": "bold"}),
                            dcc.Checklist(
                                id="product-checklist",
                                options=PRODUCT_OPTIONS,
                                value=["product_a"],          # default: Product A selected
                                labelStyle={"display": "block", "marginTop": "4px"},
                            ),
                        ],
                    ),

                    # Marker size slider
                    html.Div(
                        style={"flex": "2", "minWidth": "240px"},
                        children=[
                            html.Label("Marker Size", style={"fontWeight": "bold"}),
                            dcc.Slider(
                                id="marker-size-slider",
                                min=4,
                                max=20,
                                step=2,
                                value=10,
                                marks={i: str(i) for i in range(4, 22, 2)},
                            ),
                        ],
                    ),

                    # Line width slider
                    html.Div(
                        style={"flex": "2", "minWidth": "240px"},
                        children=[
                            html.Label("Line Width", style={"fontWeight": "bold"}),
                            dcc.Slider(
                                id="line-width-slider",
                                min=1,
                                max=6,
                                step=0.5,
                                value=2,
                                marks={i: str(i) for i in range(1, 7)},
                            ),
                        ],
                    ),
                ],
            ),

            # ── Graph ─────────────────────────────────────────────────────────
            dcc.Graph(
                id="line-graph",
                config={"displayModeBar": True, "scrollZoom": True},
                style={"height": "480px"},
            ),

            # ── Summary table placeholder ──────────────────────────────────────
            html.Div(id="summary-table", style={"marginTop": "24px"}),
        ],
    )
