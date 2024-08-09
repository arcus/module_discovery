from dash import Input, Output, State

### left_hand_nav_bar expands and contracts based on user interactions
def get_left_hand_nav_bar_callbacks(app):

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

    # Collection open/close
    @app.callback(
        Output("collection_collapse_checklist", "is_open"),
        [Input("collection_collapse_button", "n_clicks")],
        [State("collection_collapse_checklist", "is_open")],
        )
    def toggle_collapse2(n, is_open):
        if n:
            return not is_open
        return is_open

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
    
    # Level open/close
    @app.callback(
        Output("level_collapse_checklist", "is_open"),
        [Input("level_collapse_button", "n_clicks")],
        [State("level_collapse_checklist", "is_open")],
        )
    def toggle_collapse(n, is_open):
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
        Output("level_checklist", "value"),
        Output("data_task_checklist", "value"),
        Output("data_domain_checklist", "value"),
        Output("search_input", "value"),
        Output("collection_checklist", "value"),
        Input("clear_all_selections", "n_clicks"),
        prevent_initial_call=True
    )
    def clear_all_selections(n_clicks):
        if n_clicks:
            return [], '', '', '', '', '', '' , ''