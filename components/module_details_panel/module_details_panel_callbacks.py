# This callback is a function that takes one input (a module id like citizen_science)
# and returns the details with all the information we want to display about that module
# if no module name is given, this function should return some generic instruction text.


from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
from .title_link import title_link
from .connected_modules import connected_modules
from .tags import find_tags
from .learning_objectives import learning_objectives
from .pre_reqs import pre_reqs
from .add_to_my_modules import add_to_my_modules
from .remove_my_modules import remove_my_modules
from components.visualization_panels.active_module_visualization import active_module_visualization

# This is the automatically displayed metadata about the active module:
def module_info(active_node):
    # # These buttons need to be initialized to prevent errors in callbacks
    # initialize_buttons = [html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0, style = dict(display='block')) for module in list(module_data.df.index)]
    # initialize_add_to_my_modules_buttons = [html.Button("Add "+module+" to my list ", id="add_to_my_modules_"+module, n_clicks=0, style = dict(display='block')) for module in list(module_data.df.index)]
    # When a module is selected, its data is shown:
    if active_node in list(module_data.df.index):
        # These buttons need to be initialized to prevent errors in callbacks
        # other_nodes = list(module_data.df.index).copy()
        # other_nodes.remove(active_node)
        # initialize_buttons = [html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0, style = dict(display='none')) for module in other_nodes]
        #initialize_add_to_my_modules_buttons = [html.Button("Add "+module+" to my list ", id="add_to_my_modules_"+module, n_clicks=0, style = dict(display='block')) for module in other_nodes]

        module_info_panel = [#dcc.Markdown("##### Module details"),
                        title_link(active_node),
                        dbc.Row([
                            dbc.Col(add_to_my_modules(active_node), xs=6, md=3), ## This returns a single button, all the other buttons are initialized and hidden using the initialize_add_to_my_modules
                            dbc.Col(remove_my_modules(active_node), xs=6, md=4), ## This returns a single button, all the other buttons are initialized and hidden using the initialize_add_to_my_modules
                        ], justify="center"),
                        html.Br(),
                        #find_tags(active_node),
                        dcc.Markdown("By " + module_data.df.loc[active_node,'author']),
                        dcc.Markdown("Estimated length: " + module_data.df.loc[active_node,'estimated_time_in_minutes']+" minutes"),
                        dcc.Markdown(module_data.df.loc[active_node,'comment']),
                        dcc.Markdown(learning_objectives(active_node)),
                        html.Hr(),
                        pre_reqs(active_node),
                        html.Hr(),
                        # add buttons to link to preceding and following modules (or at least names for the moment).
                        html.Div(connected_modules(active_node)),
                        #html.Hr(),
                        #html.Div(initialize_buttons), 
                        #html.Div(initialize_add_to_my_modules_buttons)        
                        ]
        return module_info_panel
    else:
        # These buttons need to be initialized to prevent errors in callbacks
        initialize_buttons = [html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0, style = dict(display='none')) for module in list(module_data.df.index)]
        #initialize_add_to_my_modules_buttons = [html.Button("Add "+module+" to my list ", id="add_to_my_modules_"+module, n_clicks=0, style = dict(display='block')) for module in list(module_data.df.index)]

        return html.Div([
            dcc.Markdown("Use the buttons or click on a node in the graph to learn more about and get a link to an individual module. \n"), 
            html.Div(initialize_buttons), 
            add_to_my_modules(active_node),
            remove_my_modules(active_node)
            ])



def update_module_info_panel(app):
    @app.callback(
            Output('active_module_details_panel', 'children'),
            Input('hidden_active_module', 'children'))
    def update_module_info_panel(active_node):
        return module_info(active_node)
