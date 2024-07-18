from dash import html,  dcc
from .pre_made_pathways import pre_made_pathways 

my_modules_panel = html.Div(children=[
                #dcc.Markdown("Choose a pre-made pathway to explore! You can modify it to fit your needs, or build your own pathway from scratch."),
                #pre_made_pathways, 
                #html.Br(),
                #html.Hr(),
                html.Br(),
                html.Div([dcc.Markdown(children=["### Find a pathway or build your own \n Start with one of the popular pathways under the \"Explore Pathways\" tab, \n \n Use the \"Expore Modules\" tab to find more modules that interest you. \n \n  Add everything that interests you to your pathway."])
                ], id='display_my_modules')
                ])
                


