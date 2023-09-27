### Take input from the "Add to my list" buttons and update the my_modules list
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import ast #This allows the easy conversion from string back to dictionary

### If any add_to_my_modules buttons are pressed, that module should be added to the list of my_modules
def my_modules_in(app):
    @app.callback(Output('hidden_my_modules', 'children'),
                State("hidden_my_modules", 'children'),
                [Input("add_to_my_modules_"+module_id, 'n_clicks') for module_id in module_data.df.index], #these buttons are add_to_my_modules buttons shown on the module details panel
                prevent_initial_call=True)
    def activate(my_modules_dict,*args):
        if ctx.triggered[0]['value'] and ctx.triggered[0]['value'] > 0:
            module_to_add = ctx.triggered_id[18:]
            update_dict = ast.literal_eval(my_modules_dict)
            update_dict[module_to_add] = 1
            return str(update_dict)
        else:
            return my_modules_dict

