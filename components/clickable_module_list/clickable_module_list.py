from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 


add_all_to_my_modules = dbc.Button("Add all to my list", color="primary", id="add_filtered_to_my_modules")

clickable_module_list = html.Div(
                  [dbc.Col(
                    children=[
                     html.Div([
                        dbc.Row([
                        dbc.Col(dcc.Markdown("Modules that match your filters are listed here and visible in the graph to the right.", style={'background-color': '#ADD8E6'}), width=9),
                        dbc.Col(add_all_to_my_modules, width=3)
                    ])]),
                     html.Div([], id='clickable_module_links')
                     ]
                     
                ),
                ])
