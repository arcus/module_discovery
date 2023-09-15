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

# This is the automatically displayed metadata about the active module:
def module_info(active_node):
    # These buttons need to be initialized to prevent errors in callbacks
    initialize_buttons = [html.Button(module_data.df.loc[module,"title"], id=module+"_nottub", n_clicks=0, style = dict(display='none')) for module in list(module_data.df.index)]
    initialize_add_to_my_modules_buttons = [html.Button(module_data.df.loc[module,"title"], id="add_to_my_modules"+module, n_clicks=0, style = dict(display='none')) for module in list(module_data.df.index)]
    # When a module is selected, its data is shown:
    if active_node in list(module_data.df.index):
        module_info_panel = [dcc.Markdown("##### Module details"),
                        title_link(active_node),
                        add_to_my_modules(active_node),
                        #find_tags(active_node),
                        dcc.Markdown("By " + module_data.df.loc[active_node,'author']),
                        dcc.Markdown("Estimated length: " + module_data.df.loc[active_node,'estimated_time_in_minutes']+" minutes"),
                        dcc.Markdown(module_data.df.loc[active_node,'comment']),
                        dcc.Markdown(learning_objectives(active_node)),
                        html.Hr(),
                        pre_reqs(active_node),
                        html.Hr(),
                        html.Div(connected_modules(active_node)),
                        html.Div(initialize_buttons), 
                        html.Div(initialize_add_to_my_modules_buttons)        
                        ]
        return module_info_panel
    else:
        return html.Div([dcc.Markdown("##### Module details \n Use the buttons above or click on a node in the graph to the right to learn more about and get a link to an individual module. \n --- "), html.Div(initialize_buttons), html.Div(initialize_add_to_my_modules_buttons)])



def update_module_info_panel(app):
    @app.callback(
            Output('active_module_details_panel', 'children'),
            Input('hidden_active_module', 'children'))
    def update_module_info_panel(active_node):
        return module_info(active_node)
