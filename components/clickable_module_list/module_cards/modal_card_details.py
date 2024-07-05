from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 


def modal_module_details(module_id):
    return dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle(module_data.df.loc[module_id, "title"])),
                    dbc.ModalBody(
                        [dcc.Markdown("By " + module_data.df.loc[module_id,'author']),
                        dcc.Markdown("Estimated length: " + module_data.df.loc[module_id,'estimated_time_in_minutes']+" minutes"),
                        #dcc.Markdown(module_data.df.loc[module_id,'comment']),
                        dcc.Markdown("**Description:**"),
                        dcc.Markdown(module_data.df.loc[module_id,'long_description']),
                        dcc.Markdown("**Learning objectives:**"),
                        dcc.Markdown(module_data.df.loc[module_id,'learning_objectives']),
                        dcc.Markdown("**What should I already know?**"),
                        dcc.Markdown(module_data.df.loc[module_id,'pre_reqs'])
                        ]
                    ),
                    dbc.ModalFooter(
                        # dbc.Button(
                        #     "Close", id="modal", className="ms-auto", n_clicks=0
                        # )
                    ),
                ],
                id="modal_"+module_id,
                size="lg",
                scrollable=True,
                is_open=False,
            )

def create_clickable_module_list(app):
    for module_id in module_data.df.index:
        @app.callback(
            Output("modal_"+module_id, "is_open"),
            [Input("module_details_modal_"+module_id, "n_clicks")],
            [State("modal_"+module_id, "is_open")],
            prevent_initial_call=True
        )
        def toggle_modal(n1, is_open):
            if n1:
                return not is_open
            return is_open