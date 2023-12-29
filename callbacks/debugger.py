### Take input from all over the app to determine the unique node that is currently the ACTIVE NODE
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import ast

### Use ctx to determine whether the last thing clicked was a button or a node on the graph, then make that thing the ACTIVE NODE

module_buttons = [module_id+'_button' for module_id in module_data.df.index]

def debugger(app):
    @app.callback(Output('debugger', 'children'),
                Input('module_visualization', 'elements'))
    def show(elements):
        my_string = str(elements)
        return ast.literal_eval(my_string)