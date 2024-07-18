from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import assets.CHOP_colors as CHOP
import assets.pre_made_pathways.pathways as pathways
pathway_list = pathways.pathway_list
import module_data 

def pathway_details(pathway):
    return dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle(dcc.Markdown("## "+pathway["name"]))),
                    dbc.ModalBody(
                        [dcc.Markdown(pathway["description"]),
                         html.Hr(),
                         html.Br(),
                         dcc.Markdown("**"+pathway["name"]+"** contains "+str(len(pathway["module_list"]))+" modules:"),
                         dcc.Markdown([module_data.df.loc[module_id, "title"]+"\n \n" for module_id in pathway["module_list"]]),
                        ]
                    ),
                    dbc.ModalFooter(
                        # dbc.Button(
                        #     "Close", id="modal", className="ms-auto", n_clicks=0
                        # )
                    ),
                ],
                id="modal_"+pathway["id"],
                size="lg",
                scrollable=True,
                is_open=False,
            )

def pathway_details_modals(app):
    for pathway in pathway_list:
        @app.callback(
            Output("modal_"+pathway["id"], "is_open"),
            [Input("pathway_details_modal_"+pathway["id"], "n_clicks")],
            [State("modal_"+pathway["id"], "is_open")],
            prevent_initial_call=True
        )
        def toggle_modal(n1, is_open):
            if n1:
                return not is_open
            return is_open