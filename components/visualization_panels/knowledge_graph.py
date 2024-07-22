from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 
from stylesheets import default_stylesheet 
from network_analysis import poset_processing as poset
import assets.CHOP_colors as CHOP

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

# Define node styles:

node_styling = {
                'background-color': CHOP.light_blue,
                'label': 'data(title)',
                'color': 'black',
                "font-size": "7px",
                #'opacity': 1,
                'width': "10px",
                'height': "10px",
                "text-wrap": "wrap",
                "text-max-width": 50,
                # 'text-halign':'center',
                # 'text-valign':'center',
                # 'width':'label',
                # 'height':'label',
                # 'shape':'square'

                    }

# Define the graph edges
edges = []
for edge in poset.hasse.edges():
    edges.append({'data': {'source': edge[1], 'target': edge[0]}})


#default_stylesheet = default_stylesheet.default_stylesheet

combined_visualization_panel = dbc.Container(
                        cyto.Cytoscape(
                        id='module_visualization',
                        layout={'name': 'cose'},
                        elements=edges+nodes,
                        stylesheet = [
                                # make all the nodes neutrally styled
                                {'selector': 'node', 'style': node_styling},
                                # make all the edges neutrally styled
                                {'selector': 'edge', 'style': default_stylesheet.neutral_edge_styling},
                                ],
                        #stylesheet=default_stylesheet,
                        #style={'width': '100%', 'height':'450px%'},
                        userZoomingEnabled=True,
                        ), 
                        className = "d-flex justify-content-center", 
                        #style={'border-style': 'solid', 'border-color': '#ADD8E6', 'padding' : '25px'}
                        )