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
            ## Create buttons for each of the modules in the pathway, in the order they are currently in the list.
            total_pathway_time = 0
            for module in hidden_pathway:
                button_group = dbc.Row([dbc.Col(dbc.ButtonGroup(
                        [
                            dbc.Button("Up", color="light gray"),
                            dbc.Button("Down", color="light gray"),
                            dbc.Button(module_data.df.loc[module,"title"], color="light gray", n_clicks=0, id=module+"_nutbot"),
                        ]
                    ), width=9), dbc.Col(module_data.df.loc[module,"estimated_time_in_minutes"]+" minutes", width=2)], justify="between")
                pathway_list.append(button_group)
                pathway_list.append(html.Br())
                if len(module_data.df.loc[module,"estimated_time_in_minutes"]) == 2:
                    total_pathway_time += int(module_data.df.loc[module,"estimated_time_in_minutes"])
            
            ## Give a sum of the estimated times (NEEDS EVERY MODULE TO HAVE ESTIMATED TIME IN MINUTES FOR REAL)
            minutes = total_pathway_time % 60
            total_hours = int((total_pathway_time-minutes)/60)
            summation_line = html.Div([
                html.Hr(),
                dbc.Row([dbc.Col("Total estimated time of this pathway:",width=7), dbc.Col(str(total_hours)+" hours, "+str(minutes)+" minutes", width=3)],justify="between")
            ])
            pathway_list.append(summation_line)

            ## Create hidden buttons for the modules not in the list to prevent callback problems
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
