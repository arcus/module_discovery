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
        'position': {}
    }
    for row in df.index 
]

# Define the graph edges
edges = []
for edge in poset.hasse.edges():
    edges.append({'data': {'source': edge[1], 'target': edge[0]}})


default_stylesheet = default_stylesheet.default_stylesheet

combined_visualization_panel = dbc.Col(
                    children=[
                    html.Br(),
                    dcc.Markdown("##### Interact with this graph \n * Click on a node to learn more about it in the Module Details section. \n * Drag the nodes around to see how they are interconnected.", style={'background-color': '#FFFFFF'}),
                    dbc.Row(cyto.Cytoscape(
                        id='module_visualization',
                        layout={'name': 'cose', 
                                #'nodeDimensionsIncludeLabels': 'true',
                                #'avoidOverlap':'true'
                                },
                        elements=edges+nodes,
                        stylesheet=default_stylesheet,
                        #style={'width': '100%', 'height':'450px%'},
                        userZoomingEnabled=False
                        ), justify="center"),
                     ],
                )
