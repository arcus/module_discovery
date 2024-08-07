from dash import html, dcc
import dash_bootstrap_components as dbc
from .modal_card_details import modal_module_details
from .module_level import module_level_icon
from assets.collections import collections_icons
import assets.CHOP_colors as CHOP
import module_data 


def module_card(module_id):

  return dbc.Card(
    [
        dbc.CardHeader(dbc.Row([
          dbc.Col(collections_icons(module_id), width = 6), 
          dbc.Col(module_level_icon(module_id), width = 3), 
          dbc.Col([module_data.df.loc[module_id,'estimated_time_in_minutes']+" m"], width = 3)]),
          ),
        dbc.CardBody(
            [
                dbc.Row([html.A(module_data.df.loc[module_id,'title'],href="https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/"+ module_id +"/" + module_id + ".md" , target="_blank", className="card-title", style={'font-size':'125%', "font-weight": "bold", "color":CHOP.black}),
                
                ]),
                dcc.Markdown(module_data.df.loc[module_id,'comment'], className="card-text"),
            ],
            style={"height":'200px', "overflow":"scroll"}
        ),
        dbc.CardFooter(
          dbc.Row([dbc.Col([
                      dbc.Button("More details", id="module_details_modal_"+module_id, n_clicks=0, style={"background-color":CHOP.light_blue_tint[3], "border-width":"0px", "color":CHOP.black}),
                      
                      modal_module_details(module_id),
                      
                    ], width=5),
                dbc.Col(dbc.Button("Add to my pathway",id="add_to_my_modules_"+module_id, n_clicks=0, style={"background-color":CHOP.green_tint[3], "border-width":"0px", "color":CHOP.black}
                    ), width=7)
                ], className="center")
          )
    ],
    style={"width":"375px"},
    className="m-2",
    id="mini_card_"+module_id
)