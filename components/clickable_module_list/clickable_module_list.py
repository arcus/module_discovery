from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 


add_all_to_my_modules = html.Button("Add all to my list", id="add_filtered_to_my_modules")

remove_all_from_my_modules = html.Button("Remove all from my list", id="remove_filtered_from_my_modules")


clickable_module_list = html.Div(
                  [dbc.Col(
                    children=[
                     html.Div([
                        dbc.Col(dcc.Markdown("Modules that match your filters are listed here and visible in the graph to the right.", style={'background-color': '#ADD8E6'}), width=12),
                        dbc.Row([
                          dbc.Col(add_all_to_my_modules, width=3), 
                          dbc.Col(remove_all_from_my_modules, width=4)
                          ],
                          justify="center")
                          ]),
                    html.Br(),
                     html.Div([], id='clickable_module_links')
                     ]
                     
                ),
                ])
