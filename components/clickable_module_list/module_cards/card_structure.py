from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import module_data 


def module_card(module_id):

  return dbc.Card(
    [
        dbc.CardHeader(dbc.Row([
          dbc.Col([module_data.df.loc[module_id,'collection']], width = 8), 
          dbc.Col("level", width = 2), 
          dbc.Col([module_data.df.loc[module_id,'estimated_time_in_minutes']+" m"], width = 2)])),
        dbc.CardBody(
            [
                dbc.Row([html.A(module_data.df.loc[module_id,'title'],href="https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/"+ module_id +"/" + module_id + ".md" , target="_blank", className="card-title", style={'font-size':'125%', "font-weight": "bold"}),
                
                ]),
                dcc.Markdown(module_data.df.loc[module_id,'comment'], className="card-text"),
            ]
        ),
        dbc.CardFooter(
          dbc.Row([dbc.Col([
                      dbc.Button("More details", id="module_details_modal"+module_id, n_clicks=0),
                  dbc.Modal(
                      [
                          dbc.ModalHeader(dbc.ModalTitle("Header")),
                          dbc.ModalBody("This is the content of the modal"),
                          dbc.ModalFooter(
                              dbc.Button(
                                  "Close", id="close", className="ms-auto", n_clicks=0
                              )
                          ),
                      ],
                      id="modal",
                      is_open=False,
                    )
                    ]),
                dbc.Col(dbc.Button("Add to my list", id="123456789", n_clicks=0))
                ])
          )
    ],
    style={"width": "25rem"},
)

# @app.callback(
#     Output("modal", "is_open"),
#     [Input("open", "n_clicks"), Input("close", "n_clicks")],
#     [State("modal", "is_open")],
# )
# def toggle_modal(n1, n2, is_open):
#     if n1 or n2:
#         return not is_open
#     return is_open