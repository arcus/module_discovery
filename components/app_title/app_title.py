from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from components import mini_graph

image_path = 'assets/RI_logo.png'

branding_logo = html.A(
    href="https://www.research.chop.edu/department-of-biomedical-and-health-informatics",
    children=[
        html.Img(
            alt="Link to Children's Hospital of Philadelphia Department of Biomedical and Health Informatics",
            src=image_path,
            style={'max-width':'100%'}
        )
    ],
    target="_blank"
)

feedback_button = dbc.Button(
    "Give feedback to help us improve", 
    color="light gray", 
    n_clicks=0, 
    id="feedback_survey",
    href="https://redcap.link/module_discovery_app_feedback",
    external_link=True,
    target="_blank",
    style={"background-color":"#005587",
        "color":"white",
        "font-weight":"bold"},
    )

learn_more_button = dbc.Button(
    "Learn more about this project", 
    color="light gray", 
    n_clicks=0, 
    id="feedback_survey",
    href="https://redcap.link/module_discovery_app_feedback",
    external_link=True,
    target="_blank",
    style={"background-color":"#005587",
        "color":"white",
        "font-weight":"bold"},
    )

app_title = dbc.Row(
    [dbc.Col(branding_logo, xs=12, md =3,xl=2), 

    dbc.Col(html.B(["Module Discovery Tool Prototype"]), style={'textAlign': 'center','font-size':'40px'}, align='center',xs=12,  md=7, xl=8), 
    dbc.Col([dbc.Row(learn_more_button, justify='center'),html.Br(), dbc.Row(feedback_button, justify='center')], xs=12,xl=2),
    dbc.Col(mini_graph.mini_graph, style={'textAlign': 'center'}, xs=1,  md=2, xl=3),], justify='center')
