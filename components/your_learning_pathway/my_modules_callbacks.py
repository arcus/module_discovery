from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
from network_analysis import pathway_order_relations as p_order
from .pathway_buttons import prereqs_precede_row, prereqs_follow_row, prior_knowledge_required_row, general_pathway_buttons
import assets.CHOP_colors as CHOP
from .modal_save_pathway import modal_my_module_list

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
        
        
        ## If the pathway contains modules, display them
        if hidden_pathway != []:
            pathway_list = initialize_nutbots

            ## Sort modules button
            sort_button = dbc.Stack(children=[
                dbc.Button("Order pathway by module dependencies", color="light gray", n_clicks=0, id="sort_my_modules", style={"display":"block", "background-color":CHOP.light_blue_tint[2]}),
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
                #copyable_markdown += "["+module_data.df.loc[module,"title"]+"](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/"+module+"/"+module+".md#1) "+ module_data.df.loc[module,"estimated_time_in_minutes"]+" minutes \n \n"

                
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
            save_button = dbc.Button("Get a copyable version of your pathway", id="copy_my_modules", style={"background-color":CHOP.light_blue_tint[3], "color":CHOP.black})            

            ## Opening text
            pathway_title = dbc.Row([dbc.Col(dcc.Markdown("## **Your Pathway**"), width = 8), dbc.Col(children=[save_button, modal_my_module_list(hidden_pathway)], width = 4)], align="justify")
            return dbc.Container([pathway_title] + pathway_list, style={"max-width":"800px"})

        ## If nothing is in the pathway, display a message 
        else:
            pathway_title = dbc.Row([dbc.Col(dcc.Markdown("## **Your Pathway**"), width = 9), dbc.Col("", width = 3)], align="justify")
            empty_pathway_message = dcc.Markdown("#### You haven't selected any modules for your pathway yet.")
            sort_button = dbc.Button("Sort these modules", color="light gray", n_clicks=0, id="sort_my_modules", style={"display":"none"})
            return dbc.Container(children=[pathway_title]+initialize_nutbots+[empty_pathway_message]+[sort_button], style={"width":"800px"})
        
        #html.Div(children=initialize_nutbots+[empty_pathway_message]+[sort_button])
