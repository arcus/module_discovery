from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

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
    "Help improve this prototype by giving feedback", 
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

app_title = dbc.Row([dbc.Col(branding_logo, xs=12, md =6,xl=2), dbc.Col(html.B(["Module Discovery Tool Prototype"]), style={'textAlign': 'center','font-size':'40px'}, align='center',xs=12,  md=6, xl=8), dbc.Col(dbc.Row(feedback_button, justify='center'), xs=12,xl=2)], justify='center')
