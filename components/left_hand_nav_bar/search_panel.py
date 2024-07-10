from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data
import assets.CHOP_colors as CHOP

search_panel = dbc.Col([
    dcc.Input(id="search_input", placeholder="Search")

], width=12, style={'background-color': CHOP.light_blue_tint[2]})

def search_results(value):
    matches = []
    if value:
        for module in module_data.df.index:
            if value.lower() in str(module_data.df.loc[module,'title']).lower():
                matches.append(module)
            elif value.lower() in str(module_data.df.loc[module,'comment']).lower():
                matches.append(module)
            elif value.lower() in str(module_data.df.loc[module,'long_description']).lower():
                matches.append(module)
            elif value.lower() in str(module_data.df.loc[module,'learning_objectives']).lower():
                matches.append(module)
            elif value.lower() in str(module_data.df.loc[module,'author']).lower():
                matches.append(module)
    return matches