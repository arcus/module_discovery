from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

def add_to_my_modules(active_node):
    add_to_my_modules_buttons = []
    for module in module_data.df.index:
        button_id = "add_to_my_modules_"+str(active_node)
        if module == active_node:
            visible_button = html.Button(children=["Add "+module+" to my list "], id=button_id, style = dict(display='block'))
            add_to_my_modules_buttons.append(visible_button)
        else: 
            invisible_button = html.Button(children=["Don't add "+module+" to my list "], id=button_id, style = dict(display='none'))
            add_to_my_modules_buttons.append(invisible_button)
    return html.Div(add_to_my_modules_buttons)

