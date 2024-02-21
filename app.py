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

from components.module_details_panel import module_details_panel, module_details_panel_callbacks
module_information = module_details_panel.module_details_panel

from components.left_hand_nav_bar import search_panel
search_panel = search_panel.search_panel

from components.my_modules_panel import my_modules, my_modules_callbacks
my_modules_panel = my_modules.my_modules_panel

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
    #hidden_graph.hidden_graph,
    html.Hr(),

    # Banner heading
    dbc.Row(children=[app_title]),
    
    html.Br(),
    
    # Main body
    dbc.Row(children=[
        
        # Left hand search bar
        dbc.Col([left_hand_nav_bar], xs=12, sm=6, md=4, xxl=2,style={'background-color': '#ADD8E6'}),
        
        # Center accordion 
        dbc.Col([
            dbc.Accordion([
                # Search Results
                dbc.AccordionItem(clickable_module_list_panel, title="Search Results", item_id="search_results"), 
                # User Pathway
                dbc.AccordionItem(html.Div(my_modules_panel), title="Build Your Own Pathway", item_id="selected_modules"), 
                # Module Details
                dbc.AccordionItem(module_information, title="Module Details", item_id="module_details")
            ],
            active_item=["search_results", "selected_modules", "module_details"],
            always_open=True,
            )],
            xs=12, sm=6, md=8, xxl=5),
        
        # Right hand visualization panel
        dbc.Col(children=[
            dcc.Tabs([ ## Dash Core Components of tabs must be used, cytoscape graphs don't play nice with dbc tabs.
                dcc.Tab(combined_visualization_panel, label="Combined Visualization"),
                dcc.Tab(pathway_visualization, label="Your Pathway"),
                dcc.Tab(active_module_visualization, label="Focus on one Module"),
                dcc.Tab(search_results_visualization, label="Search Results")
            ])
        ],xs=12, sm=12, md=12, xxl=5, style={'border-style': 'solid', 'border-color': '#ADD8E6', 'padding' : '25px'}),
        
        ]),
    
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
module_details_panel_callbacks.update_module_info_panel(app)
my_modules_callbacks.show_my_modules_list(app)

# Initialize all INTERcomponent callbacks next...
callbacks.render_combined_visualization.turn_nodes_on_off(app)
clickable_module_list_callbacks.create_clickable_module_list(app)
callbacks.update_search_results.update_hidden_filtered_modules(app)
callbacks.render_search_results.show_search_results_visually(app)
callbacks.update_active_node.update_active_node(app)
callbacks.render_active_node.render_active_node(app)
callbacks.update_pathway.update_pathway(app)
callbacks.render_pathway.show_pathway_visually(app)

# turn on the debugger if using it
#callbacks.debugger.debugger(app)

if __name__ == '__main__':
    app.run_server(debug=True)