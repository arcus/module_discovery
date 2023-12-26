from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 
from stylesheets import default_stylesheet 
from network_analysis import poset_processing as poset

df = module_data.df

# Define the graph nodes
nodes = [
    {
        'data': {
            'id': row, 
            'title': df.loc[row,'title'], 
            },
    }
    for row in df.index 
]

# Define the graph edges
edges = []
for edge in poset.hasse.edges():
    edges.append({'data': {'source': edge[1], 'target': edge[0]}})


default_stylesheet = default_stylesheet.default_stylesheet

active_module_visualization = dbc.Col(
                    children=[
                    html.Br(),
                    dcc.Markdown("##### See how your selected module is connected to others \n * Click on a connected node to change the focus to that module. \n * Drag the nodes around to see how they are interconnected.", style={'background-color': '#FFFFFF'}),
                    dbc.Row(children =[cyto.Cytoscape(
                        id='active_module_visualization',
                        layout={'name': 'preset', 
                                #'nodeDimensionsIncludeLabels': 'true',
                                #'avoidOverlap':'true'
                                },
                        elements=edges+nodes,
                        stylesheet=default_stylesheet,
                        #style={'width': '100%', 'height':'450px%'},
                        userZoomingEnabled=False
                        )], 
                        justify="center",
                        ),
                     ],
                )
