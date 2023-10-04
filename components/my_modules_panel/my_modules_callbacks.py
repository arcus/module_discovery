from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import ast #This allows the easy conversion from string back to dictionary

def show_my_modules_list(app):
    @app.callback(Output('display_my_modules', 'children'),
                Input('hidden_pathway','children'),
                prevent_initial_call=True)
    def update_list(hidden_pathway):
        if hidden_pathway == []:
            return "You haven't selected any modules yet! Explore what is available and click \"Add to my list\" select the modules you want to focus on."
        else:
            pathway_list = []
            for module in hidden_pathway:
                button_group = dbc.ButtonGroup(
                        [
                            dbc.Button("Up", color="light gray"),
                            dbc.Button("Down", color="light gray"),
                            dbc.Button(module_data.df.loc[module,"title"], color="light gray", n_clicks=0, id=module+"_nutbot"),
                        ]
                    )
                pathway_list.append(button_group)
                pathway_list.append(html.Br())
            for module in [x for x in module_data.df.index if x not in hidden_pathway]:
                button_group = dbc.ButtonGroup(
                    [
                        dbc.Button("Up", color="light gray"),
                        dbc.Button("Down", color="light gray"),
                        dbc.Button(module_data.df.loc[module,"title"], color="light gray", n_clicks=0, id=module+"_nutbot"),
                    ]
                , style= {'display': 'none'})
                pathway_list.append(button_group)

            return pathway_list
