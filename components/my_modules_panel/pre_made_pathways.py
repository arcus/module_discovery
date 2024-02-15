from dash import html,  dcc
import dash_bootstrap_components as dbc

big_button_style = {"height":"auto",
                    "width":'18%'}

pre_made_pathways = dbc.Row([
    html.Button("Getting Started with Biomedical Data Science", style=big_button_style, id="pathway_1"),
    html.Button("Focus on Omics", style=big_button_style, id="pathway_2"),
    html.Button("Big Data, Big Questions", style=big_button_style, id="pathway_3"),
    html.Button("Analysis in R", style=big_button_style, id="pathway_4"),
    html.Button("Analysis in Python", style=big_button_style, id="pathway_5")
], justify="between")

