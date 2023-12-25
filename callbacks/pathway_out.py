from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import networkx as nx
import module_data 
from stylesheets import default_stylesheet 
from network_analysis import poset_processing as poset

df = module_data.df

def show_pathway_visually(app):
    @app.callback(Output('pathway_visualization', 'elements'),
                Output('pathway_visualization', 'stylesheet'),
                Input('hidden_pathway','children'),
                State('hidden_active_module', 'children'),
                prevent_initial_call=True) 
    def update_pathway_graph(hidden_pathway, active_node):
        ### Set up the subgraph created by the pathway
        pathway_subgraph = poset.hasse.subgraph(hidden_pathway)
        # Define the graph nodes
        nodes = [{'data': {'id': vertex, 'title': df.loc[vertex,'title'] }} for vertex in pathway_subgraph.nodes()]
        # Define the graph edges
        edges = [{'data': {'source': edge[1], 'target': edge[0]},  'classes': 'poset_relationship'} for edge in pathway_subgraph.edges()]
        # Add in any additional edges created by the pathway, even if those aren't graph edges
        pathway_edges = [{'data':{'source': hidden_pathway[i], 'target': hidden_pathway[i-1]}, 'classes': 'pathway_relationship'} for i in range(1, len(hidden_pathway))]
        # The elements of the graph display are the nodes and the edges:
        elements=nodes+edges+pathway_edges
        
        ### Create a new stylesheet for this induced pathway subgraph
        # Regular poset edges are still "neutral"
        new_stylesheet = [ {'selector': '.poset_relationship', 'style': default_stylesheet.neutral_edge_styling}]
        # Edges created by the pathway itself also appear
        new_stylesheet += [ {'selector': '.pathway_relationship', 'style': default_stylesheet.pathway_edge_styling}]
        
        # Node styling is that all of them are selected GET UX HELP TO FIGURE OUT IF THIS MAKES SENSE
        for module in nodes:
            module_id = module['data']['id']
            selector = str('[id *= "')+str(module_id)+str('" ]')
            # the active node should be distinguishable
            if module_id == active_node:
                new_stylesheet +=[{'selector': selector, 'style': default_stylesheet.active_node_styling}]
            # all nodes in the pathway should be labeled
            else:            
                new_stylesheet += [{'selector': selector, 'style': default_stylesheet.selected_styling}]

        return elements, new_stylesheet