from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

def add_to_my_modules(active_node):
    button_id = "add_to_my_modules_"+str(active_node)
    return html.Div(
    [
        dbc.Button("Add to my list ", id=button_id, color="primary", n_clicks=0)])

