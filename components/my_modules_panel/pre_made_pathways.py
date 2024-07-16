from dash import html,  dcc
import dash_bootstrap_components as dbc
import assets.CHOP_colors as CHOP
import assets.pre_made_pathways.pathways as pathways
pathway_list = pathways.pathway_list
from .pathway_card_details import pathway_details

def pathway_card(pathway):
    card = dbc.Card(
    [
        dbc.CardHeader(dbc.Row(pathway["name"])),
        dbc.CardBody(
            [
                dcc.Markdown(pathway["comment"],
                    #className="card-text",
                )]),
        dbc.CardFooter(          
            dbc.Row([dbc.Col([
                      dbc.Button("More details", id="pathway_details_modal_"+pathway["id"], n_clicks=0, style={"background-color":CHOP.light_blue_tint[3], "border-width":"0px", "color":CHOP.black}),
                      
                      pathway_details(pathway)
                    ]),
                #dbc.Col(dbc.Button("Email this to me", n_clicks=0, style={"background-color":CHOP.pink_tint[3], "border-width":"0px", "color":CHOP.black})),
                
                dbc.Col(dbc.Button("Add to my list", n_clicks=0, style={"background-color":CHOP.green_tint[3], "border-width":"0px", "color":CHOP.black}))
                ])),
    ],
    style={"width":"420px"},
    className="m-2"
    )
    return card

pre_made_pathways = dbc.Container([pathway_card(pathway) for pathway in pathway_list], 
                                  className="d-flex flex-wrap justify-content-center")