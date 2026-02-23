"""
callbacks.py — All Dash callback definitions.

Importing this module registers every callback automatically via the
@callback decorator (Dash 2.x global registration — no app reference needed).

Callbacks
---------
1. populate_category_dropdown
       Trigger : page load (dcc.Location pathname)
       Output  : category-dropdown options

2. update_subcategory_dropdown
       Trigger : category-dropdown value
       Outputs : subcategory-dropdown options, value, disabled flag

3. update_table
       Triggers: category-dropdown value, subcategory-dropdown value
       Outputs : products-table data, status-text children
"""

from dash import Input, Output, callback

from data import get_categories, get_subcategories, get_products


# ── 1. Populate Dropdown 1 on initial page load ────────────────────────────────

@callback(
    Output("category-dropdown", "options"),
    Input("_url", "pathname"),          # dcc.Location fires once on mount
)
def populate_category_dropdown(_pathname: str) -> list[dict]:
    """
    Fill Dropdown 1 with top-level category options.

    Uses the page URL as a trigger so this fires automatically when the
    browser first renders the app — no user interaction required.
    """
    return get_categories()


# ── 2. Cascade: sync Dropdown 2 whenever Dropdown 1 changes ───────────────────

@callback(
    Output("subcategory-dropdown", "options"),
    Output("subcategory-dropdown", "value"),
    Output("subcategory-dropdown", "disabled"),
    Input("category-dropdown", "value"),
)
def update_subcategory_dropdown(category: str | None) -> tuple:
    """
    When the user picks (or clears) a category:
      • Repopulate sub-category options to match the selected category.
      • Reset the sub-category selection to None so stale values don't linger.
      • Disable Dropdown 2 when no category is selected (guard against
        showing an empty, confusing dropdown).
    """
    if not category:
        return [], None, True           # empty options, cleared, disabled

    subcategory_options = get_subcategories(category)
    return subcategory_options, None, False


# ── 3. Update DataTable when either dropdown changes ──────────────────────────

@callback(
    Output("products-table", "data"),
    Output("status-text",    "children"),
    Input("category-dropdown",    "value"),
    Input("subcategory-dropdown", "value"),
)
def update_table(
    category: str | None,
    subcategory: str | None,
) -> tuple[list[dict], str]:
    """
    Refresh the DataTable rows whenever either dropdown changes.

    Logic
    -----
    • Neither selected  → empty table, prompt user to start with DD1.
    • Only DD1 selected → empty table, prompt user to pick a sub-category.
    • Both selected     → load matching product rows and show a breadcrumb.
    """
    if not category:
        return [], "← Select a category to get started."

    if not subcategory:
        return [], f"Showing: {category}  ›  select a sub-category to view products."

    products = get_products(category, subcategory)
    status   = f"Showing: {category}  ›  {subcategory}  —  {len(products)} product(s)"

    return products, status
