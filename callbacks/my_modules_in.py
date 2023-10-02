### Take input from the "Add to my list" buttons and update the my_modules list
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import ast #This allows the easy conversion from string back to dictionary

### If any add_to_my_modules buttons are pressed, that module should be added to the list of my_modules
def my_modules_in(app):
    @app.callback(Output('hidden_my_modules', 'children'),
                State("hidden_my_modules", 'children'),
                Input("add_filtered_to_my_modules", 'n_clicks'),
                Input("remove_filtered_from_my_modules", 'n_clicks'),
                State("hidden_filtered_modules_list", 'children'),
                [Input("add_to_my_modules_"+module_id, 'n_clicks') for module_id in module_data.df.index], #these buttons are add_to_my_modules buttons shown on the module details panel
                [Input("remove_my_modules_"+module_id, 'n_clicks') for module_id in module_data.df.index], #these buttons are remove_my_modules buttons shown on the module details panel
                prevent_initial_call=True)
    def activate(my_modules_dict,add_filtered_to_my_modules,remove_filtered_from_my_modules,hidden_filtered_modules_list,*args):

        if ctx.triggered_id == "add_filtered_to_my_modules":
            update_dict = ast.literal_eval(my_modules_dict)
            for module in list(hidden_filtered_modules_list):
                update_dict[str(module)] = 1
            return str(update_dict)
        
        elif ctx.triggered_id == "remove_filtered_from_my_modules":
            update_dict = ast.literal_eval(my_modules_dict)
            for module in list(hidden_filtered_modules_list):
                update_dict[str(module)] = 0
            return str(update_dict)

        elif ctx.triggered[0]['value'] and ctx.triggered[0]['value'] > 0:
            if ctx.triggered_id[:6] == "add_to":
                module_to_add = ctx.triggered_id[18:]
                update_dict = ast.literal_eval(my_modules_dict)
                update_dict[module_to_add] = 1
            elif ctx.triggered_id[:6] == "remove":
                module_to_remove = ctx.triggered_id[18:]
                update_dict = ast.literal_eval(my_modules_dict)
                update_dict[module_to_remove] = 0
            return str(update_dict)
        
        else:
            return my_modules_dict

