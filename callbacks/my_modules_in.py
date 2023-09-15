### Take input from the "Add to my list" buttons and update the my_modules list
from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 

### If any add_to_my_modules buttons are pressed, that module should be added to the list of my_modules
def my_modules_in(app):
    @app.callback(Output('hidden_my_modules', 'children'),
                #Input("hidden_my_modules", 'children'),
                [Input("add_to_my_modules"+module_id, 'n_clicks') for module_id in module_data.df.index], #these buttons are add_to_my_modules buttons shown on the module details panel
                #[Input("remove_from_my_modules"+module_id, 'n_clicks') for module_id in module_data.df.index], #these buttons are remove from my modules buttons shown on the module details panel
                prevent_initial_call=False)
    def activate(*args):
        # trigger = ctx.triggered_id
        # if trigger == "module_visualization":
        #     return data['id']
        # elif sum(args) != 0:
        #      return trigger[:-7]
        # else:
        return "no_module_in_list"

