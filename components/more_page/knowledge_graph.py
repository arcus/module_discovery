import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 
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

# Define node and edge styles:

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
                    }
neutral_edge_styling = {
        'color': "lightgray",
        'opacity': .4,
        'width': '2px',
        'mid-source-arrow-shape': 'vee',
         }

# Define the graph edges
edges = []
for edge in poset.hasse.edges():
    edges.append({'data': {'source': edge[1], 'target': edge[0]}})

combined_visualization_panel = dbc.Container(
                        cyto.Cytoscape(
                        id='module_visualization',
                        layout={'name': 'cose'},
                        elements=edges+nodes,
                        stylesheet = [
                                # style the nodes
                                {'selector': 'node', 'style': node_styling},
                                # style the edges
                                {'selector': 'edge', 'style': neutral_edge_styling},
                                ],
                        userZoomingEnabled=True,
                        ), 
                        className = "d-flex justify-content-center", 
                        )