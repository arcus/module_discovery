# This callback is a function that takes one input (a module id like citizen_science)
# and returns the details with all the information we want to display about that module
# if no module name is given, this function should return some generic instruction text.


from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data
import networkx as nx
from network_analysis.poset_processing import hasse

# Create a list (previously tried buttons but had circlular callback issues) for all of the connected modules using module_data.df info
def connected_modules(active_module):
    
    sets_you_up_markdown_list="\n "
    for mod in hasse.neighbors(active_module):
        sets_you_up_markdown_list = sets_you_up_markdown_list + "\n - "+module_data.df.loc[mod,"title"]

    #sets_you_up_button_list = [html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0) for module in hasse.neighbors(active_module)]
    
    depends_on_markdown_list="\n "
    for mod in hasse.reverse().neighbors(active_module):
        depends_on_markdown_list = depends_on_markdown_list + "\n - "+module_data.df.loc[mod,"title"]

    #depends_on_button_list = [html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0) for module in hasse.reverse().neighbors(active_module)]

    #neighborhood_of_active_node = list(hasse.reverse().neighbors(active_module))+list(hasse.neighbors(active_module))+[active_module]
    
    #other_nodes = [node for node in hasse.nodes() if node not in neighborhood_of_active_node]

    #hidden_button_list = [html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0, style={"display":"none"}) for module in other_nodes]

        
    left_subpanel = dbc.Col([dcc.Markdown("Not quite ready for this module? Check out these first:"+depends_on_markdown_list)], width=6) if len(list(hasse.reverse().neighbors(active_module)))>0 else dbc.Col([dcc.Markdown("This module doesn't require any specialized knowledge to get started, so check it out now!")], width=6)
    
    right_subpanel = dbc.Col([dcc.Markdown("Already familiar with this material? Try these next:"+sets_you_up_markdown_list)], width=6) if len(list(hasse.neighbors(active_module)))>0 else dbc.Col([dcc.Markdown("Use the search bar and other filters to explore other modules you might be interested in.")], width=6)
    
    return [dbc.Row([left_subpanel, right_subpanel])]#, html.Div(hidden_button_list)]
