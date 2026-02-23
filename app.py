"""
app.py — Application entry point.

Responsibilities
----------------
* Instantiate the Dash app.
* Attach the layout (from layout.py).
* Register all callbacks (from callbacks.py — side-effect import).
* Start the development server when run directly.

File structure
--------------
app.py       — this file (entry point)
layout.py    — UI component tree
callbacks.py — all @callback-decorated functions
data.py      — raw data + helper functions used by callbacks
"""

import dash

import callbacks          # noqa: F401 — registers all @callback decorators
from layout import create_layout

app = dash.Dash(__name__, title="Product Catalogue Explorer")
app.layout = create_layout()

if __name__ == "__main__":
    app.run(debug=True)
