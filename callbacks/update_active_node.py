### Take input from all over the app to determine the unique node that is currently the ACTIVE NODE
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

### Use ctx to determine whether the last thing clicked was a button or a node on the graph, then make that thing the ACTIVE NODE
def update_active_node(app):
    @app.callback(Output('hidden_active_module', 'children'),
                State('hidden_active_module', 'children'),
                Input('module_visualization', 'tapNodeData'),
                #Input('pathway_visualization', 'tapNodeData'),
                #Input('search_results_visualization', 'tapNodeData'),
                Input('active_module_visualization', 'tapNodeData'),
                [Input(module_id+"_button", 'n_clicks') for module_id in module_data.df.index], #these buttons are the buttons for the filtered module list
                #[Input(module_id+"_nottub", 'n_clicks') for module_id in module_data.df.index], #these "nottub"s are modules connected to `sets_you_up_for`s and `depends_on_knowledge_available_in`s connected to the current active node
                [Input(module_id+"_nutbot", 'n_clicks') for module_id in module_data.df.index], #these "nutbot"s are the buttons in the pathway/my_modules list.
                prevent_initial_call=True)
    def activate(current_active_node,module_visualization_data, active_node_visualization_data, *args):
        trigger = ctx.triggered_id
        if trigger == "module_visualization":
            return module_visualization_data['id']
        elif trigger == "pathway_visualization":
            return pathway_visualization_data['id']
        elif trigger == "active_module_visualization":
            return active_node_visualization_data['id']
        elif trigger == "search_results_visualization":
            return search_results_visualization_data['id']
        
        ### Something about this argument is likely what is creating the bug where when you add or remove a module from the pathway the active node goes back to bash_103_combining_commands, the first module in the list of all modules
        elif trigger[-7:] in ["_button", "_nottub", "_nutbot"]:
            ### Make sure that we aren't triggering the callback by initializing the buttons, i.e. that they have actually been clicked at least once.
            if sum(args) > 0:
                return trigger[:-7]
            else:
                return current_active_node
        else:
            return current_active_node