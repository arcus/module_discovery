from dash import html,  dcc
import dash_bootstrap_components as dbc
import assets.CHOP_colors as CHOP
import assets.pre_made_pathways.pathways as pathways
pathway_list = pathways.pathway_list
from .pathway_card_details import pathway_details


big_button_style = {"height":"auto",
                    "width":'18%'}


def pathway_card(pathway):
    card = dbc.Card(
    [
        dbc.CardHeader(dbc.Row(pathway["name"])),
        dbc.CardBody(
            [
                dcc.Markdown(pathway["comment"],
                    className="card-text",
                ),
        dbc.CardFooter(          
            dbc.Row([dbc.Col([
                      dbc.Button("More details", id="pathway_details_modal_"+pathway["id"], n_clicks=0, style={"background-color":CHOP.light_blue_tint[3], "border-width":"0px", "color":CHOP.black}),
                      
                      pathway_details(pathway)
                    ]),
                dbc.Col(dbc.Button("Add to my list", id="123456789", n_clicks=0, style={"background-color":CHOP.green_tint[3], "border-width":"0px", "color":CHOP.black}))
                ]))
            ]
        ),
    ],
    style={"width":"30%"},
    )
    return card

pre_made_pathways = dbc.Row([pathway_card(pathway) for pathway in pathway_list]
, justify="between")

# pre_made_pathways = dbc.Row([
#     html.Button("Get Started with Data Science in Biomedicine", style=big_button_style, id="pathway_1"),
#     html.Button("Focus on Omics", style=big_button_style, id="pathway_2"),
#     html.Button("Big Data, Big Questions", style=big_button_style, id="pathway_3"),
#     html.Button("Analysis in R", style=big_button_style, id="pathway_4"),
#     html.Button("Analysis in Python", style=big_button_style, id="pathway_5")
# ], justify="between")