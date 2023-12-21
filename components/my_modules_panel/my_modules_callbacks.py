from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import ast #This allows the easy conversion from string back to dictionary

def show_my_modules_list(app):
    @app.callback(Output('display_my_modules', 'children'),
                Input('hidden_pathway','children'),
                prevent_initial_call=False) # An initial call needs to be made here to initialize all the buttons
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
            empty_pathway_message = dcc.Markdown("You haven't selected any modules yet! Explore what is available and click \"Add to my list\" to create your own pathway of modules you want to focus on.")
            sort_button = dbc.Button("Sort these modules", color="light gray", n_clicks=0, id="sort_my_modules", style={"display":"none"})
            return html.Div(children=initialize_nutbots+[empty_pathway_message]+[sort_button])
            
        else:
            pathway_list = initialize_nutbots
            ## Opening text
            pathway_list.append(dcc.Markdown("Here are the modules you have selected. \n \n Use the up and down buttons to reorder them. \n"))
            ## Sort modules button
            sort_button = dbc.Stack(children=[
                dbc.Button("Sort these modules", color="light gray", n_clicks=0, id="sort_my_modules", style={"display":"block"}),
                dbc.Badge("?", id="sort_my_modules_button", pill=True,  color="light", text_color="dark"),
                dbc.Popover(
                    dbc.PopoverBody(dcc.Markdown("This ensures that if you have two modules in your pathway and one depends on knowledge available in the other based on our metadata, they will be listed in the correct order below. \n \n It does NOT ensure that sequential or related modules are next to each other, so make sure to use the up and down buttons to fine tune the order of pathway.")),
                    target="sort_my_modules_button",
                    trigger="click",
                    )], direction="horizontal")
            pathway_list.append(sort_button)

            ## Create buttons for each of the modules in the pathway, in the order they are currently in the list.
            total_pathway_time = 0
            copyable_markdown = ""
            for module in hidden_pathway:
                button_group = dbc.Row([dbc.Col(dbc.ButtonGroup(
                        [
                            dbc.Button('\U00002191', color="light gray", n_clicks=0,id=module+"_move_up"),
                            dbc.Button('\U00002193', color="light gray", n_clicks=0, id=module+"_go_down"),
                            dbc.Button(module_data.df.loc[module,"title"], color="light gray", n_clicks=0, id=module+"_nutbot"),
                        ]
                    ), width=9), dbc.Col(module_data.df.loc[module,"estimated_time_in_minutes"]+" minutes", width=2)], justify="between")
                pathway_list.append(button_group)

                copyable_markdown += "["+module_data.df.loc[module,"title"]+"](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/"+module+"/"+module+".md#1) "+ module_data.df.loc[module,"estimated_time_in_minutes"]+" minutes \n \n"
                
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

            
            pathway_list.append(dbc.Button("Save this pathway", id="copy_my_modules"))
            pathway_list.append(dbc.Popover(
                                dbc.PopoverBody(children=[
                                    dcc.Markdown("**Copy these links and paste them into a document or email for future reference:**"),
                                    dcc.Markdown(children=[copyable_markdown])], style={'width':'475px'}),
                                target="copy_my_modules",
                                trigger="click",
                                style={"max-width":"500px"},
                                
                            ) )

            return pathway_list
