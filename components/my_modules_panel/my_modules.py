from dash import html,  dcc
from .pre_made_pathways import pre_made_pathways 

my_modules_panel = html.Div(children=[
                dcc.Markdown("Choose a pre-made pathway to explore! You can modify it to fit your needs, or build your own pathway from scratch."),
                pre_made_pathways, 
                html.Br(),
                html.Hr(),
                html.Br(),
                html.Div([dcc.Markdown(children=["You haven't selected any modules yet! Explore what is available and click \"Add to my list\" to create your own pathway of modules you want to focus on."])
                ], id='display_my_modules')
                ])
                


