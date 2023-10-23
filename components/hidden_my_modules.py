## THIS IS NO LONGER BEING USED AND CAN LIKELY BE DELETED

from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data

my_module_dictionary = {id: 0 for id in module_data.df.index}

hidden_my_modules = [#dcc.Markdown("current active node"),
    html.Div(children= str(my_module_dictionary), 
    id = 'hidden_my_modules', 
    style= {'display': 'none'} # make this 'none' to hide it for final version, 'block' shows this data on the app
    )]