from dash import html
import dash_bootstrap_components as dbc
import assets.CHOP_colors as CHOP

image_path = 'assets/chop-ri--arcuslogo.png'

branding_logo = html.A(
    href="https://www.research.chop.edu/applications/arcus",
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
    id="about_page",
    href="https://github.com/arcus/module_discovery/blob/main/about.md#about-the-module-discovery-tool-prototype",
    external_link=True,
    target="_blank",
    style={"background-color":"#005587",
        "color":"white",
        "font-weight":"bold"},
    )

app_title = dbc.Row(
    [dbc.Col(branding_logo, xs=12, md =3,xl=2), 

    dbc.Col(html.B(["Data Education Navigator Tool Prototype"]), style={'textAlign': 'center','font-size':'40px', "color":CHOP.dark_blue}, align='center',xs=12,  md=9, xl=10), 
    #dbc.Col([dbc.Row(learn_more_button, justify='center'),html.Br(), dbc.Row(feedback_button, justify='center')], xs=12,xl=2),
], justify='center')
