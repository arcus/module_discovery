from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import ast #This allows the easy conversion from string back to dictionary

def show_my_modules_list(app):
    @app.callback(Output('display_my_modules', 'children'),
                Input('hidden_pathway','children'),
                prevent_initial_call=True)
    def update_list(hidden_pathway):

        ## Create hidden buttons for the modules not in the list to prevent callback problems
        initialize_nutbots = []
        for module in [x for x in module_data.df.index if x not in hidden_pathway]:
            button_group = dbc.ButtonGroup(
                [
                    dbc.Button("Up", color="light gray", n_clicks=0, id=module+"_move_up"),
                    dbc.Button("Down", color="light gray", n_clicks=0, id=module+"_go_down"),
                    dbc.Button(module_data.df.loc[module,"title"], color="light gray", n_clicks=0, id=module+"_nutbot"),
                ]
            , style= {'display': 'none'})
            initialize_nutbots.append(button_group)
        
        if hidden_pathway == []:
            empty_pathway_message = dcc.Markdown("You haven't selected any modules yet! Explore what is available and click \"Add to my list\" select the modules you want to focus on.")

            return html.Div(children=initialize_nutbots+[empty_pathway_message])
        else:
            pathway_list = initialize_nutbots
            pathway_list.append(dcc.Markdown("Here are the modules you have selected. \n \n In the future you will be able to use the up and down buttons to reorder them. \n"))
            ## Create buttons for each of the modules in the pathway, in the order they are currently in the list.
            total_pathway_time = 0
            for module in hidden_pathway:
                button_group = dbc.Row([dbc.Col(dbc.ButtonGroup(
                        [
                            dbc.Button('\U00002191', color="light gray", n_clicks=0,id=module+"_move_up"),
                            dbc.Button('\U00002193', color="light gray", n_clicks=0, id=module+"_go_down"),
                            dbc.Button(module_data.df.loc[module,"title"], color="light gray", n_clicks=0, id=module+"_nutbot"),
                        ]
                    ), width=9), dbc.Col(module_data.df.loc[module,"estimated_time_in_minutes"]+" minutes", width=2)], justify="between")
                pathway_list.append(button_group)
                ## if the estimated_time_in_minutes exists and makes sense, add it to total pathway time
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

            return pathway_list
