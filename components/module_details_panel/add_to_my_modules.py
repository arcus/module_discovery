from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

def add_to_my_modules(active_node):
    if active_node in list(module_data.df.index):
        # Make the visible button
        button_id = "add_to_my_modules_"+str(active_node)
        visible_button = html.Button(children=["Add "+active_node+" to my list "], id=button_id, style = dict(display='block'))
        # Make all the other buttons hidden
        other_nodes = list(module_data.df.index).copy()
        other_nodes.remove(active_node)
        hidden_buttons = [html.Button("Add "+module+" to my list ", id="add_to_my_modules_"+module, style = dict(display='none')) for module in other_nodes]
        hidden_buttons.append(visible_button)
        return html.Div(hidden_buttons)
    else:
        # If no node is active, make all the buttons hidden
        return html.Div([html.Button("Add "+module+" to my list ", id="add_to_my_modules_"+module, style = dict(display='none')) for module in module_data.df.index])
