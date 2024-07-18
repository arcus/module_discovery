from dash import html,  dcc
import dash_bootstrap_components as dbc
import assets.CHOP_colors as CHOP
import assets.pre_made_pathways.pathways as pathways
pathway_list = pathways.pathway_list
from .pathway_card_details import pathway_details
import module_data 

def pathway_length(pathway):
    total_time = 0
    for module in pathway["module_list"]:
        total_time += int(module_data.df.loc[module, "estimated_time_in_minutes"])
    return total_time

def pathway_card(pathway):
    card = dbc.Card(
    [
        dbc.CardHeader(dbc.Row([
          dbc.Col("", width = 6), 
          dbc.Col("", width = 3), 
          dbc.Col("~ "+str(int(pathway_length(pathway)/60))+" hours", width = 3)]),
          ),
        dbc.CardBody(
            [
                html.A(pathway["name"], style={'font-size':'125%', "font-weight": "bold"}),
                dcc.Markdown(pathway["comment"],
                    #className="card-text",
                )]),
        dbc.CardFooter(          
            dbc.Row([dbc.Col([
                      dbc.Button("More details", id="pathway_details_modal_"+pathway["id"], n_clicks=0, style={"background-color":CHOP.light_blue_tint[3], "border-width":"0px", "color":CHOP.black}),
                      
                      pathway_details(pathway)
                    ]),
                
                dbc.Col(dbc.Button("Choose pathway", id="use_"+pathway["id"], n_clicks=0, style={"background-color":CHOP.green_tint[3], "border-width":"0px", "color":CHOP.black}))
                ])),
    ],
    style={"width":"420px"},
    className="m-1"
    )
    return card

pre_made_pathway_text = "\n \n ## Popular pathways \n \n Our modules are designed to be flexible and bite-sized, so you can use your time efficiently and pick just the topics you want to study. Each module has learning objectives and prerequisites clearly listed on the first page, to help you decide which ones you want to work on. \n \n That said, many learners prefer to start with a curated list of suggestions, rather than browsing through the modules on their own. If you’re trying to figure out how to get started learning, see if one of the suggested pathways below sounds like a good fit! \n \n"

pre_made_pathways = [
    html.Br(),
    dcc.Markdown(pre_made_pathway_text),
    dbc.Container([pathway_card(pathway) for pathway in pathway_list], 
                                  className="d-flex flex-wrap justify-content-center",
                                  fluid=True)]