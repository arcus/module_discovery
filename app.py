from dash import Dash, html
import dash_bootstrap_components as dbc
import assets.CHOP_colors as CHOP

# Import the module data as a dataframe
import module_data
df = module_data.df

# Import app components and callbacks

## App Title

from components.app_title import app_title
app_title = app_title.app_title

## Explore Modules tab:

### Left-hand navigation bar

from components.explore_modules.left_hand_nav_bar import left_hand_nav_bar, left_hand_nav_bar_callbacks, search_panel
left_hand_nav_bar = left_hand_nav_bar.left_hand_nav_bar
search_panel = search_panel.search_panel

### Search results

from components.explore_modules.clickable_module_list import clickable_module_list, clickable_module_list_callbacks
clickable_module_list_panel = clickable_module_list.clickable_module_list

import callbacks.update_search_results

from components.explore_modules.clickable_module_list.module_cards import modal_card_details
modal_card_pop_up = modal_card_details.modal_card_pop_up

## Explore Pathways tab:

from components.explore_pathways import pathway_card_details, pre_made_pathways
modal_pathway_pop_up = pathway_card_details.pathway_details_modals

## Your Learning Pathways tab:

from components.your_learning_pathway import my_modules, my_modules_callbacks
your_learning_pathway = my_modules.your_learning_pathway

from components.your_learning_pathway import modal_save_pathway
pre_made_pathways = pre_made_pathways.pre_made_pathways
modal_copy_my_module_list = modal_save_pathway.modal_copy_my_module_list

import callbacks.update_pathway

## Talk to an Educator and More tabs:

from components.talk_to_educator import talk_to_educator_text
from components.more_page.more_page import more_text, show_network_graph

## Hidden components on which the app relies:
from components import hidden_filtered_modules, hidden_pathway 
hidden_filtered_modules = hidden_filtered_modules.hidden_filtered_modules
hidden_pathway = hidden_pathway.hidden_pathway

# For debugging, un-comment this:
#import callbacks.debugger




# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True) ## suppress_callback_exceptions prevents all of the errors from callbacks calling things not yet set up by other callbacks.
server = app.server


# Set up the layout of the app
app.layout = dbc.Container([
    
    # Banner heading
    dbc.Row(children=[app_title]),
    
    html.Br(),
    
    # Main body has 5 tabs:
    dbc.Row(
        dbc.Tabs([
            dbc.Tab(dbc.Row(children=[
                        
                        # Left hand search bar
                        dbc.Col([left_hand_nav_bar], xs=12, sm=4, md=3, xxl=2,style={'background-color': CHOP.light_blue_tint[1]}),
                        
                        # Center search results 
                        dbc.Col([clickable_module_list_panel], style={'background-color': CHOP.light_blue_tint[1]})
                         ]),
                    label="Explore Modules", 
                    label_style={"color":CHOP.dark_blue}, 
                    tab_id="explore_modules_tab",
                    activeTabClassName="fw-bold",
                    style={"background-color": CHOP.light_blue_tint[1]}
                    ),
            dbc.Tab(talk_to_educator_text, 
                    label="Talk to an Educator", 
                    label_style={"color":CHOP.dark_blue}, 
                    activeTabClassName="fw-bold",
                    tab_id="talk_to_educator_tab",
                    ),
            dbc.Tab(pre_made_pathways, 
                    label="Explore Pathways", 
                    label_style={"color":CHOP.dark_blue},                    
                    activeTabClassName="fw-bold",
                    tab_id="explore_pathways_tab"
                    ),
            dbc.Tab(your_learning_pathway, 
                    label="Your Learning Pathway", 
                    label_style={"color":CHOP.dark_blue}, 
                    activeTabClassName="fw-bold",
                    tab_id="your_learning_pathway_tab",
                    ),
            dbc.Tab(more_text, 
                    label="More", 
                    label_style={"color":CHOP.dark_blue}, 
                    activeTabClassName="fw-bold",
                    tab_id="more_tab",
                    ),
        ],
        active_tab="explore_modules_tab",
        id="navigation_tabs"
        )
        ),
    html.Div(hidden_filtered_modules), # DONT COMMENT OUT this is visible for debugging purposes, change to 'display': 'none' for production purposes. 
    html.Div(hidden_pathway), # DONT COMMENT OUT this is visible for debugging purposes, change to 'display': 'none' for production purposes.
    #html.Div(children=["blue"], id="debugger"),     html.Div(children=["blue"], id="debugger2")
    ],
    style={'padding' : '25px'},
    fluid=True)

# Initialize all callbacks

## Explore Modules page:
left_hand_nav_bar_callbacks.get_left_hand_nav_bar_callbacks(app) # Lets users expand and collapse fields in the left-hand search bar
callbacks.update_search_results.update_hidden_filtered_modules(app) # Generates a list of modules that match user input to left-hand search bar
clickable_module_list_callbacks.create_clickable_module_list(app) # Makes only the module cards of modules that match user's search terms visible

## Your Learning Pathway page
my_modules_callbacks.show_my_modules_list(app) # Displays the user's pathway 
modal_copy_my_module_list(app) # Opens the copyable links based on the users current pathway

## Explore Pathways page
modal_pathway_pop_up(app) # Displays the modal description of the pre-made pathways

## More page
show_network_graph(app) # Displays a modal of the network graph :)

## Multi-page callbacks
modal_card_pop_up(app) # Opens the module details modal whether the module name is clicked on the Explore Modules page or the Your Learning Pathway page
callbacks.update_pathway.update_pathway(app) # Updates the user's pathway based on interactions on the Explore Modules, Explore Pathways, and Your Learning Pathway pages.
callbacks.update_pathway.add_pathway_chage_tab(app)

# turn on the debugger if using it
#callbacks.debugger.debugger(app)

if __name__ == '__main__':
    app.run_server(debug=True)