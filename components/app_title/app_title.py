from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import base64

image_path = 'assets/RI_logo.png'

# Using base64 encoding and decoding
def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
      image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


app_title = dbc.Row([dbc.Col(html.Img(src=b64_image(image_path), style={'height':'90%', 'width':'90%'}), width =2), dbc.Col(html.B(["Module Discovery"]), style={'textAlign': 'center','font-size':'40px'}, align='end'), dbc.Col(html.Img(src=b64_image(image_path), style={'height':'90%', 'width':'90%'}), width =2)])
