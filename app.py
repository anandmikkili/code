"""
Plotly Dash App — 2 Dropdowns + DataTable
==========================================
Data source : pandas DataFrame (data.py)
Layout      : defined separately in layout.py
Callbacks   : defined separately in callbacks.py

Run
---
    python app.py
Then open http://127.0.0.1:8050 in your browser.
"""

import dash
from layout import create_layout
import callbacks  # noqa: F401 — registers callbacks as a side-effect

app = dash.Dash(__name__, title="Sales Dashboard — Dropdowns & Table")
app.layout = create_layout(app)

if __name__ == "__main__":
    app.run(debug=True)
