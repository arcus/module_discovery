from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto

# Import the module data as a dataframe
import module_data
df = module_data.df

# Import app components and their internal callbacks
from components.left_hand_nav_bar import left_hand_nav_bar, left_hand_nav_bar_callbacks 
left_hand_nav_bar = left_hand_nav_bar.left_hand_nav_bar

from components.visualization_panels import combined_visualization_panel, pathway_visualization, active_module_visualization, search_results_visualization
combined_visualization_panel = combined_visualization_panel.combined_visualization_panel
pathway_visualization = pathway_visualization.pathway_visualization
active_module_visualization = active_module_visualization.active_module_visualization
search_results_visualization = search_results_visualization.search_results_visualization

from components.app_title import app_title
app_title = app_title.app_title

from components.clickable_module_list import clickable_module_list, clickable_module_list_callbacks
clickable_module_list_panel = clickable_module_list.clickable_module_list

#
##
###
#### NEW STUFF!!!
from components.clickable_module_list.module_cards import modal_card_details
modal_card_pop_up = modal_card_details.create_clickable_module_list

import assets.CHOP_colors as CHOP

from components.my_modules_panel import pathway_card_details
modal_pathway_pop_up = pathway_card_details.pathway_details_modals

from components.my_modules_panel import pre_made_pathways
pre_made_pathways = pre_made_pathways.pre_made_pathways
#####
###
##
#

from components.module_details_panel import module_details_panel, module_details_panel_callbacks
module_information = module_details_panel.module_details_panel

from components.left_hand_nav_bar import search_panel
search_panel = search_panel.search_panel

from components.my_modules_panel import my_modules, my_modules_callbacks
my_modules_panel = my_modules.my_modules_panel

from components import exploratory_graph
exploratory_graph = exploratory_graph.exploratory_graph

# Import the hidden components that keep track of the filtered modules and the active module
from components import hidden_filtered_modules, hidden_active_module, hidden_pathway 
hidden_filtered_modules = hidden_filtered_modules.hidden_filtered_modules
hidden_active_module = hidden_active_module.hidden_active_module
hidden_pathway = hidden_pathway.hidden_pathway

# Import inter-component callbacks
import callbacks.render_combined_visualization
import callbacks.update_active_node
import callbacks.render_active_node
import callbacks.update_search_results
import callbacks.render_search_results
import callbacks.debugger
import callbacks.update_pathway
import callbacks.render_pathway


# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True) ## suppress_callback_exceptions prevents all of the errors from callbacks calling things not yet set up by other callbacks.
server = app.server


# Set up the layout of the app
app.layout = dbc.Container([

    # Visualizations being tested out:
    #html.Hr(),

    # Banner heading
    dbc.Row(children=[app_title]),
    
    html.Br(),
    
    # Main body
    dbc.Row(
        dbc.Tabs([
            dbc.Tab(dbc.Row(children=[
                
                # Left hand search bar
                dbc.Col([left_hand_nav_bar], xs=12, sm=6, md=4, xxl=2,style={'background-color': CHOP.light_blue_tint[2]}),
                
                # Center search results 
                dbc.Col([clickable_module_list_panel])
                ]),
                label="Explore Modules", 
                label_style={"color":CHOP.dark_blue}, 
                style={"background-color":CHOP.light_blue_tint[1]},
                tab_style={"background_color":CHOP.light_blue_tint[1]}),
            dbc.Tab(pre_made_pathways, label="Explore Pathways", label_style={"color":CHOP.dark_blue}),
            dbc.Tab("User created pathway goes here", label="Your Learning Pathway", label_style={"color":CHOP.dark_blue}),
            dbc.Tab("Links to office hours, etc.", label="Talk to an Educator", label_style={"color":CHOP.dark_blue}),
        ]
        )
        ),
    
    #html.Hr(), html.Hr(),
    html.Div(hidden_filtered_modules), # DONT COMMENT OUT this is visible for debugging purposes, change to 'display': 'none' for production purposes. 
    html.Div(hidden_active_module), # DONT COMMENT OUT this is visible for debugging purposes, change to 'display': 'none' for production purposes.
    html.Div(hidden_pathway), # DONT COMMENT OUT this is visible for debugging purposes, change to 'display': 'none' for production purposes.
    #html.Div(children=["blue"], id="debugger"),     html.Div(children=["blue"], id="debugger2")
    ],
    style={'padding' : '25px'},
    fluid=True)

# Initialize all INTRAcomponent callbacks
left_hand_nav_bar_callbacks.get_left_hand_nav_bar_callbacks(app)
#module_details_panel_callbacks.update_module_info_panel(app)
#my_modules_callbacks.show_my_modules_list(app)

# Initialize all INTERcomponent callbacks next...
#callbacks.render_combined_visualization.turn_nodes_on_off(app)
clickable_module_list_callbacks.create_clickable_module_list(app)

modal_card_pop_up(app)
modal_pathway_pop_up(app)

callbacks.update_search_results.update_hidden_filtered_modules(app)

#callbacks.render_search_results.show_search_results_visually(app)
#callbacks.update_active_node.update_active_node(app)
#callbacks.render_active_node.render_active_node(app)
#callbacks.update_pathway.update_pathway(app)
#callbacks.render_pathway.show_pathway_visually(app)

# turn on the debugger if using it
#callbacks.debugger.debugger(app)

if __name__ == '__main__':
    app.run_server(debug=True)