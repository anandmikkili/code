"""
Regional Sales Dashboard
========================
Two chained dropdowns (Region → Product) drive a monthly sales DataTable.

Layout   : defined in layout.py
Callbacks: defined in callbacks.py
Data     : defined in data.py
"""

import dash
from layout import create_layout
import callbacks  # noqa: F401 — registers callbacks as a side-effect

app = dash.Dash(__name__, title="Regional Sales Dashboard")
app.layout = create_layout(app)

if __name__ == "__main__":
    app.run(debug=True)
