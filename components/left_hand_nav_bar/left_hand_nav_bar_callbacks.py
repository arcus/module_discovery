from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto

### left_hand_nav_bar expands and contracts based on user interactions
def get_left_hand_nav_bar_callbacks(app):
    
    # Coding language open/close
    @app.callback(
        Output("coding_language_collapse_checklist", "is_open"),
        [Input("coding_language_collapse_button", "n_clicks")],
        [State("coding_language_collapse_checklist", "is_open")],
        )
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open
    
    # General options open/close
    @app.callback(
        Output("general_options_collapse_checklist", "is_open"),
        [Input("general_options_collapse_button", "n_clicks")],
        [State("general_options_collapse_checklist", "is_open")],
        )
    def toggle_collapse2(n, is_open):
        if n:
            return not is_open
        return is_open
    
    # Coding level open/close
    @app.callback(
        Output("coding_level_collapse_checklist", "is_open"),
        [Input("coding_level_collapse_button", "n_clicks")],
        [State("coding_level_collapse_checklist", "is_open")],
        )
    def toggle_collapse3(n, is_open):
        if n:
            return not is_open
        return is_open
    
    # Data task open/close
    @app.callback(
        Output("data_task_collapse_checklist", "is_open"),
        [Input("data_task_collapse_button", "n_clicks")],
        [State("data_task_collapse_checklist", "is_open")],
        )
    def toggle_collapse3(n, is_open):
        if n:
            return not is_open
        return is_open
    
    # Data domain open/close
    @app.callback(
        Output("data_domain_collapse_checklist", "is_open"),
        [Input("data_domain_collapse_button", "n_clicks")],
        [State("data_domain_collapse_checklist", "is_open")],
        )
    def toggle_collapse3(n, is_open):
        if n:
            return not is_open
        return is_open
    
    # Clear selections button
    @app.callback(Output("general_options_checklist", "value"),
        Output("coding_language_checklist", "value"),
        Output("coding_level_checklist", "value"),
        Output("data_task_checklist", "value"),
        Output("data_domain_checklist", "value"),
        Output("search_input", "value"),
        Input("clear_all_selections", "n_clicks"),
        prevent_initial_call=True
    )
    def clear_all_selections(n_clicks):
        if n_clicks:
            return [], '', '', '', '', ''