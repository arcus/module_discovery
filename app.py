from dash import Dash, html, Input, Output, dcc, ctx, State
# Consider adding details, e.g.
# ctx offers context information that is helpful in callbacks, such as the ID of the element
# that was the trigger of the callback (note: is this true?  I'm just flailing here).  

import dash_bootstrap_components as dbc
import dash_cytoscape as cyto

# Import the module data as a dataframe
import module_data
df = module_data.df

# Import styling from assets directory
from assets import default_stylesheet 

# Import app components and their internal callbacks
from components.left_hand_nav_bar import left_hand_nav_bar, left_hand_nav_bar_callbacks 
left_hand_nav_bar = left_hand_nav_bar.left_hand_nav_bar

from components.visualization_panel import visualization_panel
visualization_panel = visualization_panel.visualization_panel

from components.app_title import app_title
app_title = app_title.app_title

from components.heading_tabs import heading_tabs
heading_tabs = heading_tabs.heading_tabs

from components.clickable_module_list import clickable_module_list, clickable_module_list_callbacks
clickable_module_list_panel = clickable_module_list.clickable_module_list

from components.module_details_panel import module_details_panel, module_details_panel_callbacks
module_information = module_details_panel.module_details_panel

from components.left_hand_nav_bar import search_panel
search_panel = search_panel.search_panel

from components.my_modules_panel import my_modules, my_modules_callbacks
my_modules_panel = my_modules.my_modules_panel

# Import the hidden components that keep track of the filtered modules and the active module
from components import hidden_filtered_modules, hidden_active_module, hidden_my_modules, hidden_pathway
hidden_filtered_modules = hidden_filtered_modules.hidden_filtered_modules
hidden_active_module = hidden_active_module.hidden_active_module
hidden_my_modules = hidden_my_modules.hidden_my_modules
hidden_pathway = hidden_pathway.hidden_pathway

# Import inter-component callbacks
import callbacks.stylesheet_callbacks
import callbacks.active_node_in
import callbacks.active_node_out
import callbacks.filter_modules_in
import callbacks.debugger
#import callbacks.my_modules_in
import callbacks.pathway_in





# Initialize the app
app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           suppress_callback_exceptions=True) ## suppress_callback_exceptions prevents all of the errors from callbacks calling things not yet set up by other callbacks.
server = app.server


# Set up the layout of the app
app.layout = html.Div([
    dbc.Row(children=[
        app_title,
        ]
        ),
    html.Hr(),
    dbc.Row(children=[
        left_hand_nav_bar,
        dbc.Col([
            dbc.Accordion([
                dbc.AccordionItem(clickable_module_list_panel, title="Search Results", item_id="search_results"), 
            #html.Hr(), html.Br(), 
                dbc.AccordionItem(html.Div(my_modules_panel), title="Selected Modules", item_id="selected_modules"), 
            #html.Hr(), html.Br(),
                dbc.AccordionItem(module_information, title="Module Details", item_id="module_details")
            ],
            active_item=["search_results", "selected_modules", "module_details"],
            always_open=True,
            )],
            xs=12, lg = 8, xl = 5),
        dbc.Col(children=[visualization_panel
        ],xs=12, lg = 8, xl = 5),
        
        
        ]),
    html.Hr(), html.Hr(),
    html.Div(hidden_filtered_modules), # DONT COMMENT OUT this is visible for debugging purposes, change to 'display': 'none' for production purposes. 
    html.Div(hidden_active_module), # DONT COMMENT OUT this is visible for debugging purposes, change to 'display': 'none' for production purposes.
    html.Div(hidden_pathway), # DONT COMMENT OUT this is visible for debugging purposes, change to 'display': 'none' for production purposes.
    #html.Div(children=["blue"], id="debugger"),     html.Div(children=["blue"], id="debugger2")
    ],
    style={'padding' : '25px'}
    )

# Initialize all INTRAcomponent callbacks
left_hand_nav_bar_callbacks.get_left_hand_nav_bar_callbacks(app)
module_details_panel_callbacks.update_module_info_panel(app)
my_modules_callbacks.show_my_modules_list(app)

# Initialize all INTERcomponent callbacks next...
callbacks.stylesheet_callbacks.turn_nodes_on_off(app)
clickable_module_list_callbacks.create_clickable_module_list(app)
callbacks.filter_modules_in.update_hidden_filtered_modules(app)
callbacks.active_node_in.active_node_in(app)
#callbacks.active_node_out.active_node_out(app)
callbacks.debugger.debugger(app)
#callbacks.my_modules_in.my_modules_in(app)
callbacks.pathway_in.pathway_in(app)

if __name__ == '__main__':
    app.run_server(debug=True)