from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import module_data 
from assets import default_stylesheet 
import networkx as nx

df = module_data.df

# Create a networkx graph with module ids as its vertices
G = nx.DiGraph()
G.add_nodes_from(df.index)

# Add directed edges from depends_on_knowledge_in and sets_you_up_for
for module_id in df.index:
    for linked_module in df.index:
        if str(linked_module) in str(df.loc[module_id, "sets_you_up_for"]):
            G.add_edge(module_id, linked_module)
        if str(linked_module) in str(df.loc[module_id, "depends_on_knowledge_available_in"]):
            G.add_edge(linked_module, module_id)

# Build maximal and minimal directed acyclic graphs
poset = nx.transitive_closure(G)
hasse = nx.transitive_reduction(G)

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
for edge in hasse.edges():
    edges.append({'data': {'source': edge[1], 'target': edge[0]}})


default_stylesheet = default_stylesheet.default_stylesheet

visualization_panel = dbc.Col(
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
