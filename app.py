"""
Sample Plotly Dash App — Line Graph with Markers
=================================================
Data source : pandas DataFrame
Layout      : defined separately in `layout.py`
Callback    : defined separately in `callbacks.py`
"""

import dash
from layout import create_layout
import callbacks  # noqa: F401 — registers callbacks as a side-effect

app = dash.Dash(__name__, title="Line Graph with Markers")
app.layout = create_layout(app)

if __name__ == "__main__":
    app.run(debug=True)
