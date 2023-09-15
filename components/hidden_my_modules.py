from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc

hidden_my_modules = [#dcc.Markdown("current active node"),
    html.Div(children=["dummy"], 
    id = 'hidden_my_modules', 
    style= {'display': 'block'} # make this 'none' to hide it for final version, 'block' shows this data on the app
    )]