from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import base64

image_path = 'assets/RI_logo.png'

# Using base64 encoding and decoding
def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
      image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')

branding_logo = html.A(
    href="https://www.research.chop.edu/department-of-biomedical-and-health-informatics",
    children=[
        html.Img(
            alt="Link to Children's Hospital of Philadelphia Department of Biomedical and Health Informatics",
            src=b64_image(image_path),
            style={'width':'90%'}
        )
    ],
    target="_blank"
)

feedback_button = dbc.Button(
    "Give feedback on this prototype", 
    color="light gray", 
    n_clicks=0, 
    id="feedback_survey",
    href="https://redcap.link/module_discovery_app_feedback",
    external_link=True,
    target="_blank"
    )

app_title = dbc.Row([dbc.Col(branding_logo, width =2), dbc.Col(html.B(["Module Discovery Tool Prototype"]), style={'textAlign': 'center','font-size':'40px'}, align='end'), dbc.Col(feedback_button, width =2)])
