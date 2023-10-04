from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data

my_pathway = []

hidden_pathway = [
    html.Div(children=my_pathway, 
    id = 'hidden_pathway', 
    style= {'display': 'block'} # make this 'none' to hide it for final version, 'block' shows this data on the app
    )]