from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import networkx as nx
import module_data 
from assets import default_stylesheet 
from network_analysis import poset_processing as poset

df = module_data.df

def show_pathway_visually(app):
    @app.callback(Output('testing', 'children'),
                Input('hidden_pathway','children'),
                prevent_initial_call=True) 
    def update_pathway_graph(hidden_pathway):
        # Set up the subgraph created by the pathway
        pathway_subgraph = poset.G.subgraph(hidden_pathway)
        # Define the graph nodes
        nodes = [{'data': {'id': vertex, 'title': df.loc[vertex,'title'] }} for vertex in pathway_subgraph.nodes()]
        # Define the graph edges
        edges = [{'data': {'source': edge[1], 'target': edge[0]}} for edge in pathway_subgraph.edges()]
        pathway = cyto.Cytoscape(
                        id='pathway_visualization',
                        layout={'name': 'cose'},
                        elements=edges+nodes,
                        stylesheet=default_stylesheet,
                        #style={'width': '100%', 'height':'450px%'},
                        userZoomingEnabled=False
                        )
        
        return str(pathway) #pathway
