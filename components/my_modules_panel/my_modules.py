from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import ast #This allows the easy conversion from string back to dictionary


my_modules_panel = html.Div(children=[
                dcc.Markdown(children=["You haven't selected any modules yet! Explore what is available and click \"Add to my list\" select the modules you want to focus on."])
                ], id='display_my_modules')


