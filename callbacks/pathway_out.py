from dash import Dash, html, Input, Output, dcc, ctx, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import networkx as nx
import module_data 
from stylesheets import default_stylesheet, pathway_stylesheet
from network_analysis import poset_processing as poset
import ast

df = module_data.df

def show_pathway_visually(app):
    @app.callback(Output('pathway_visualization', 'elements'),
                Output('pathway_visualization', 'stylesheet'),
                Output('debugger', 'children'),
                Input('hidden_pathway','children'),
                State('hidden_active_module', 'children'),
                State('module_visualization','elements'),
                prevent_initial_call=True) 
    def update_pathway_graph(hidden_pathway, active_node, raw_element_data):
        ### import all nodes and position data from the module_visualization
        element_data = ast.literal_eval(str(raw_element_data))

        ### Set up the subgraph created by the pathway
        pathway_subgraph = poset.hasse.subgraph(hidden_pathway)


        # # Define the graph nodes
        # nodes = [{'data': {'id': vertex, 'title': df.loc[vertex,'title'] }} for vertex in pathway_subgraph.nodes()]
        # # Define the graph edges
        # edges = [{'data': {'source': edge[1], 'target': edge[0]},  'classes': 'poset_relationship'} for edge in pathway_subgraph.edges()]


        # Add in any additional edges created by the pathway, even if those aren't graph edges
        pathway_edges = [{'data':{'source': hidden_pathway[i], 'target': hidden_pathway[i-1]}, 'classes': 'pathway_relationship'} for i in range(1, len(hidden_pathway))]
        # The elements of the graph display are the nodes and the edges:
        elements=element_data+pathway_edges
        
        ### Create a new stylesheet for this induced pathway subgraph
        # Initialize the non-pathway styling for all nodes and edges
        new_stylesheet = [ {'selector': 'edge', 'style': pathway_stylesheet.non_pathway_edge_styling}]
        new_stylesheet += [ {'selector': 'node', 'style': pathway_stylesheet.non_pathway_node_styling}]
        # Edges created by the pathway itself also appear
        new_stylesheet += [ {'selector': '.pathway_relationship', 'style': pathway_stylesheet.pathway_edge_styling}]
        
        # Node styling is that all of them are selected GET UX HELP TO FIGURE OUT IF THIS MAKES SENSE
        for module_id in pathway_subgraph.nodes():
            selector = str('[id *= "')+str(module_id)+str('" ]')
            # the active node should be distinguishable
            if module_id == active_node:
                new_stylesheet +=[{'selector': selector, 'style': default_stylesheet.active_node_styling}]
            # all nodes in the pathway should be labeled
            else:            
                new_stylesheet += [{'selector': selector, 'style': pathway_stylesheet.pathway_node_styling}]

        #
        element_data = ast.literal_eval(str(raw_element_data))[0]
        return elements, new_stylesheet, str(element_data)