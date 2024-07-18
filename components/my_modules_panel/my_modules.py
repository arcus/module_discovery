from dash import html,  dcc
import dash_bootstrap_components as dbc
from .pre_made_pathways import pre_made_pathways 

my_modules_panel = html.Div(children=[
                html.Br(),
                dbc.Container(dcc.Markdown("## Find a pathway or build your own \n \n Start from scratch or build off one of the popular pathways under the \"Explore Pathways\" tab. \n \n Use the \"Expore Modules\" tab to find more modules that interest you. \n \n  Come back here to the \"Your Learning Pathway\" tab to remove and reorder the modules in your pathway.")),
                #pre_made_pathways, 
                #html.Br(),
                #html.Hr(),
                html.Br(),
                dbc.Container([dcc.Markdown(children=["Your pathway, or text about what to do now."])
                ], id='display_my_modules')
                ])
                


