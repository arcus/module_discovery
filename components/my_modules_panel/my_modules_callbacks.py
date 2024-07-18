from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
from network_analysis import pathway_order_relations as p_order
import ast #This allows the easy conversion from string back to dictionary
from .pathway_buttons import prereqs_precede_row, prereqs_follow_row, prior_knowledge_required_row, general_pathway_buttons

def show_my_modules_list(app):
    @app.callback(Output('display_my_modules', 'children'),
                Input('hidden_pathway','children'),
                prevent_initial_call=False) # An initial call needs to be made here to initialize all the buttons
    def update_list(hidden_pathway):

        ## Create hidden buttons for the modules not in the list to prevent callback problems
        initialize_nutbots = []
        for module in [x for x in module_data.df.index if x not in hidden_pathway]:
            button_group = html.Div(general_pathway_buttons(module), style= {'display': 'none'})
            initialize_nutbots.append(button_group)
        
        ## If nothing is in the pathway, display a message 
        if hidden_pathway == []:
            empty_pathway_message = dcc.Markdown("### Find a pathway or build your own \n \n Start from scratch or build off one of the popular pathways under the \"Explore Pathways\" tab. \n \n Use the \"Expore Modules\" tab to find more modules that interest you. \n \n  Come back to the \"Your Learning Pathway\" tab to remove and reorder the modules in your pathway.")
            sort_button = dbc.Button("Sort these modules", color="light gray", n_clicks=0, id="sort_my_modules", style={"display":"none"})
            return html.Div(children=initialize_nutbots+[empty_pathway_message]+[sort_button])
        
        ## If the pathway contains modules, display them
        else:
            pathway_list = initialize_nutbots

            ## Sort modules button
            sort_button = dbc.Stack(children=[
                dbc.Button("Order pathway by module dependencies", color="light gray", n_clicks=0, id="sort_my_modules", style={"display":"block"}),
                dbc.Badge("?", id="sort_my_modules_button", pill=True,  color="light", text_color="dark"),
                dbc.Popover(
                    dbc.PopoverBody(dcc.Markdown("This ensures that if you have two modules in your pathway and one depends on knowledge available in the other based on our metadata, they will be listed in the correct order below. \n \n It does NOT ensure that sequential or related modules are next to each other, so make sure to use the up and down buttons to fine tune the order of pathway.")),
                    target="sort_my_modules_button",
                    trigger="hover",
                    )], direction="horizontal")
            pathway_list.append(sort_button)

            headings = dbc.Row([
                dbc.Col([], width=2),
                dbc.Col([dcc.Markdown("**Modules in your pathway**")], width=7),
                dbc.Col([],width=1), 
                dbc.Col([dcc.Markdown("**Length**")], width=2)],
                justify="between")

            pathway_list.append(html.Br())
            
            pathway_list.append(headings)
            #pathway_list.append(html.Hr())

            ## Create buttons for each of the modules in the pathway, in the order they are currently in the list.
            total_pathway_time = 0
            copyable_markdown = ""
            for module in hidden_pathway:
                if p_order.prereqs_precede(hidden_pathway, module):
                    pathway_list.append(prereqs_precede_row(hidden_pathway,module))

                elif p_order.prereqs_follow(hidden_pathway, module):
                    pathway_list.append(prereqs_follow_row(hidden_pathway, module))

                else:
                    pathway_list.append(prior_knowledge_required_row(hidden_pathway,module))

                # Add the module to the copyable text version of the pathway
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
            pathway_list.append(html.Br())

            ## Button to allow user to copy their pathway and save it somewhere else
            save_button = [dbc.Button("Save this pathway", id="copy_my_modules"),
                            dbc.Popover(
                                dbc.PopoverBody(children=[
                                    dcc.Markdown("**Copy these links and paste them into a document or email for future reference:**"),
                                    dcc.Markdown(children=[copyable_markdown])], style={'width':'475px'}),
                                target="copy_my_modules",
                                trigger="click",
                                style={"max-width":"500px"},
                                
                            )]
            ## Opening text
            pathway_title = dbc.Row([dbc.Col(dcc.Markdown("## **Your Pathway**"), width = 9), dbc.Col(save_button, width = 3)], align="justify")
            return dbc.Container([pathway_title] + pathway_list, style={"width":"800px"})
