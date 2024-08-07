### Take input from all over the app to determine the unique node that is currently the ACTIVE NODE
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import ast
from network_analysis.poset_processing import hasse

### Use ctx to determine whether the last thing clicked was a button or a node on the graph, then make that thing the ACTIVE NODE

module_buttons = [module_id+'_button' for module_id in module_data.df.index]

def debugger(app):
    @app.callback(Output('debugger', 'children'),
                [Input(module_id+"_nottub", 'n_clicks') for module_id in module_data.df.index], #these "nottub"s are modules connected to `sets_you_up_for`s and `depends_on_knowledge_available_in`s connected to the current active node
)
    def show(*args):
        return ctx.triggered_id