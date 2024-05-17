from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from network_analysis import poset_processing as poset
from network_analysis import required_expertise_times

from stylesheets import default_stylesheet 
default_stylesheet = default_stylesheet.default_stylesheet

from stylesheets import required_expertise_stylesheet

required_expertise_styling = required_expertise_stylesheet.required_expertise_stylesheet
import module_data 

df = module_data.df


# Define the graph nodes
nodes = [
    {
        'data': {
            'id': row, 
            'title': df.loc[row,'title'], 
            'expertise_required': int(required_expertise_times.required_expertise_times(row))/500
            },
    }
    for row in df.index 
]

# Define the graph edges
edges = []
for edge in poset.hasse.edges():
    edges.append({'data': {'source': edge[1], 'target': edge[0]}})

exploratory_graph = html.Div(
    dbc.Row(
            cyto.Cytoscape(
            id='hidden_graph',
            layout={'name': 'cose'},
            elements=nodes+edges,
            stylesheet=required_expertise_styling,
            #stylesheet=default_stylesheet,
            #style={'height':'10px', 'center':True},
            userZoomingEnabled=False,
            userPanningEnabled=True,
            responsive=True,
            ), 
        justify="center"
        ),
    style={"maxHeight": "450px"},
)