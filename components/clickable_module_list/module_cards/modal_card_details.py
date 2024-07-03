from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 


def modal_module_details(module_id):
    return dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Header")),
                    dbc.ModalBody("This is the content of the modal for "+module_id),
                    dbc.ModalFooter(
                        # dbc.Button(
                        #     "Close", id="modal", className="ms-auto", n_clicks=0
                        # )
                    ),
                ],
                id="modal_"+module_id,
                is_open=False,
            )

def create_clickable_module_list(app):
  @app.callback(
      [Output("modal_bash_103_combining_commands", "is_open")],
      [Input("module_details_modal_bash_103_combining_commands", "n_clicks") #for module_id in module_data.df.index
      #Input("close", "n_clicks")
      ],
      [State("modal_bash_103_combining_commands", "is_open")],
  )
  def toggle_modal(n1, is_open):
      if n1:# or n2:
          return not is_open
      return is_open