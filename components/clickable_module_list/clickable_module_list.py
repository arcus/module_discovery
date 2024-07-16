from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import assets.CHOP_colors as CHOP
import module_data 


add_all_to_my_modules = dbc.Button("Add all to my pathway", id="add_filtered_to_my_modules", style={"background-color":CHOP.green_tint[2], "border-width":"0px", "color":CHOP.black})

remove_all_from_my_modules = dbc.Button("Remove all from my pathway", id="remove_filtered_from_my_modules", style={"background-color":CHOP.green_tint[2], "border-width":"0px", "color":CHOP.black})


clickable_module_list = html.Div(
                  [dbc.Col(
                    children=[
                     html.Div([
                        html.Br(),
                        dbc.Col(dcc.Markdown("Modules that match your filters and search terms are listed here."), width=12, id="search_results_message"),
                        dbc.Row([
                          dbc.Col(add_all_to_my_modules, xs=6,md=3), 
                          dbc.Col(remove_all_from_my_modules, xs=6, md=4)
                          ],
                          justify="center"),
                        html.Br()
                          ], style={'background-color':CHOP.light_blue_tint[1]}),
                    #html.Br(),
                     html.Div([], id='clickable_module_links', 
                              style={"maxHeight": "650px", "overflow": "scroll"}, 
                              className="col-12")
                     ]       
                ),
                ],
                style={"background-color":CHOP.light_blue_tint[1]}
                )
