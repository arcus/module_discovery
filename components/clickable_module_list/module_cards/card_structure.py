from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
from .modal_card_details import modal_module_details
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
                      dbc.Button("More details", id="module_details_modal_"+module_id, n_clicks=0),
                      modal_module_details(module_id)
                    ]),
                dbc.Col(dbc.Button("Add to my list", id="123456789", n_clicks=0))
                ])
          )
    ],
    style={"width": "25rem"},
)

# def create_clickable_module_list(app):
#   @app.callback(
#       [Output("modal_"+module_id, "is_open") for module_id in module_data.df.index],
#       [Input("module_details_modal_bash_103_combining_commands", "n_clicks") #for module_id in module_data.df.index
#       #Input("close", "n_clicks")
#       ],
#       [State("modal_bash_103_combining_commands", "is_open")],
#   )
#   def toggle_modal(n1, is_open):
#       if n1:# or n2:
#           return not is_open
#       return is_open