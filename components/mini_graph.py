from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from network_analysis import poset_processing as poset
import module_data 

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

mini_graph = html.Div(
    dbc.Row(
            cyto.Cytoscape(
            id='hidden_graph',
            layout={'name': 'cose'},
            elements=nodes+edges,
            #stylesheet=default_stylesheet,
            style={'height':'10px', 'center':True},
            userZoomingEnabled=False,
            userPanningEnabled=True,
            responsive=True,
            ), 
        justify="center"
        ),
    style={"maxHeight": "150px"},
)