from dash import html, Input, Output, dcc, State
import dash_bootstrap_components as dbc
import module_data 
import re

## Removing links from this text is important because markdown links open in the same window, not target = _blank, and navigating away from the webpage might lose the user's pathway.
def no_links(markdown_text):
    link_free_text = markdown_text
    for markdown_link in markdown_text:
        link_free_text = re.sub('\[([^\]]+)\]\(http[^ ]+\)', '\\1',  link_free_text)
    return link_free_text


def modal_module_details(module_id):
    return dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle(module_data.df.loc[module_id, "title"])),
                    dbc.ModalBody(
                        [dcc.Markdown("By " + module_data.df.loc[module_id,'author']),
                        dcc.Markdown("Estimated length: " + module_data.df.loc[module_id,'estimated_time_in_minutes']+" minutes"),
                        dcc.Markdown("**Description:**"),
                        dcc.Markdown(no_links(module_data.df.loc[module_id,'long_description'])),
                        dcc.Markdown("**Learning objectives:**"),
                        dcc.Markdown(no_links(module_data.df.loc[module_id,'learning_objectives'])),
                        dcc.Markdown("**What should I already know?**"),
                        html.A(no_links(module_data.df.loc[module_id,'pre_reqs']))
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

def modal_card_pop_up(app):
    for module_id in module_data.df.index:
        @app.callback(
            Output("modal_"+module_id, "is_open"),
            [Input("module_details_modal_"+module_id, "n_clicks")],
            [Input(module_id+"_nutbot", "n_clicks")],
            [State("modal_"+module_id, "is_open")],
            prevent_initial_call=True
        )
        def toggle_modal(n1, n2, is_open):
            if n1 or n2:
                return not is_open
            return is_open