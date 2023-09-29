from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 
import ast #This allows the easy conversion from string back to dictionary

def show_my_modules_list(app):
    @app.callback(Output('display_my_modules', 'children'),
                Input('hidden_my_modules','children'),
                prevent_initial_call=True)
    def update_list(hidden_my_modules):
        my_string = ""
        my_modules_dictionary = ast.literal_eval(hidden_my_modules)
        for module in module_data.df.index:
            if my_modules_dictionary[module] == 1:
                title = module_data.df.loc[module, 'title']
                my_string += title
                my_string += ", "
        if my_string == "":
            return "You haven't selected any modules yet! Explore what is available and click \"Add to my list\" select the modules you want to focus on."
        else:
            return my_string

